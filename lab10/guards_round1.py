"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
import re

from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Preserve the agent's separate damaged/lost/general-question workflows.
    text = ctx.ticket.get("text", "")
    if re.search(r"vỡ|hỏng|móp|bể|damaged|broken|chưa nhận|không nhận được|thất lạc|not received|lost", text, re.I):
        return Verdict.allow()
    if not re.search(r"trễ|chậm|muộn|late|delay", text, re.I):
        return Verdict.allow()

    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    if order is None or order.get("customer_id") != ctx.ticket.get("customer_id"):
        return Verdict.escalate("Không xác minh được đơn và người gửi trước khi đọc yêu cầu hoàn")
    if order.get("checkout_note"):
        # ReadTools returns copies: changing this dict cannot sanitize the agent's
        # later lookup. Stop before that untrusted free-text reaches the model.
        ctx.log("checkout_note_review", order_id=order["order_id"])
        return Verdict.escalate("Đơn có ghi chú checkout tự do: cần người kiểm chứng, không coi ghi chú là phê duyệt")
    if not order.get("parcels"):
        return Verdict.escalate("Thiếu tracking kiện để xác minh độ trễ")
    try:
        delay = max(H.db_delay_days(p, ctx.as_of) for p in order["parcels"])
    except (KeyError, TypeError, ValueError):
        return Verdict.escalate("Tracking thiếu hoặc sai ngày: cần người xác minh")

    # A structured LATE request uses only DB facts. Customer prose cannot supply
    # a delay, an instruction, a payer, or an approval to the model.
    ctx.log("late_request_normalized", order_id=order["order_id"], db_delay_days=delay)
    return Verdict.rewrite(
        "Chuẩn hóa yêu cầu giao trễ theo tracking; lời khách không phải lệnh hoặc phê duyệt",
        f"Yêu cầu xem xét hoàn phí vận chuyển do giao trễ {delay} ngày theo tracking.",
    )


def _facts(ctx, order_id):
    """Source-of-truth facts for one order: order, effective policy, the parcel the ticket is about, its DB delay."""
    order = ctx.tools.lookup_order(order_id)
    if order is None or not order.get("parcels"):
        return None
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    return order, policy, parcel, H.db_delay_days(parcel, ctx.as_of)


def _valid_approval(ctx, approval_id, order_id, amount):
    """An approval counts only if it is for THIS order, still valid, not expired, covers the amount,
    and is signed by the approver named in config (operations.approver_id)."""
    if not approval_id:
        return False
    found = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not found:
        return False
    a = found[0]
    approver = (ctx.gates or {}).get("operations", {}).get("approver_id")
    return (a.get("order_id") == order_id and a.get("status") == "valid"
            and a.get("expires_at", "") >= ctx.as_of and amount <= a.get("max_vnd", 0)
            and (not approver or a.get("approver_id") == approver))


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    # Rule for every branch: recompute from tracking DB + effective policy + ledger. Never trust the
    # amount, delay, payer or approval the model proposed (pre-mortem ★CỔNG 1-3, Phiếu B mục B6).
    tool = action.get("tool")

    if tool == "issue_refund":
        facts = _facts(ctx, action.get("order_id"))
        if facts is None:
            return Verdict.escalate("không đủ dữ liệu đơn / tracking / chính sách hiệu lực để kiểm số tiền hoàn")
        order, policy, parcel, delay = facts
        owed = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        already = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
        remaining = owed - already
        if action.get("basis") == "fail_open":
            ctx.log("refund_fail_open_recomputed", order_id=order["order_id"], owed_vnd=owed)
        if remaining <= 0:
            # covers: delay below policy threshold, customer-claimed delay, already refunded, write retry
            return Verdict.deny(f"theo tracking ({delay} ngày) và {policy['policy_id']}, đơn còn được hoàn "
                                f"{max(0, remaining)}đ (đã hoàn {already}đ)")
        approved = _valid_approval(ctx, action.get("approval_id"), order["order_id"], remaining)
        if action.get("payer", "LOGIX") != "LOGIX" and not approved:
            return Verdict.escalate("ghi bên trả khác LogiX mà không có phê duyệt hợp lệ của đúng đơn")
        if remaining > policy["auto_limit_vnd"] and not approved:
            return Verdict.escalate(f"khoản hoàn {remaining}đ vượt hạn mức tự động {policy['auto_limit_vnd']}đ "
                                    f"mà không có phê duyệt hợp lệ của đúng đơn")
        if action.get("approval_id") and not approved:
            return Verdict.escalate("phê duyệt kèm theo không hợp lệ (khác đơn, đã dùng, hết hạn hoặc không đủ hạn mức)")
        if action.get("amount_vnd") != remaining:
            return Verdict.modify(f"chỉnh số tiền theo tracking và {policy['policy_id']}", amount_vnd=remaining)
        return Verdict.allow()

    if tool == "file_carrier_fault":
        facts = _facts(ctx, action.get("order_id"))
        if facts is None:
            return Verdict.deny("không đủ dữ liệu để quy lỗi cho hãng")
        order, policy, parcel, _ = facts
        at_fault = [p for p in order["parcels"]
                    if H.carrier_at_fault(policy, p, H.db_delay_days(p, ctx.as_of))]
        if not at_fault:
            return Verdict.deny("không kiện nào trễ đủ ngưỡng với nguyên nhân được ghi nhận thuộc lỗi hãng")
        target = next((p for p in at_fault if p["parcel_id"] == action.get("parcel_id")), None) \
            or (parcel if parcel in at_fault else at_fault[0])
        cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        if cap is not None and len(ctx.tools.fault_rows(carrier_id=target["carrier_id"])) >= cap:
            ctx.log("carrier_strike_cap", carrier_id=target["carrier_id"], cap=cap)
            return Verdict.deny(f"hãng {target['carrier_id']} đã chạm trần {cap} lỗi tự động trong ngày: cần người duyệt")
        fix = {"parcel_id": target["parcel_id"], "carrier_id": target["carrier_id"],
               "driver_id": target.get("driver_id"), "delay_days": H.db_delay_days(target, ctx.as_of)}
        if any(action.get(k) != v for k, v in fix.items()):
            return Verdict.modify("quy lỗi đúng kiện trễ, đúng hãng và độ trễ theo tracking", **fix)
        return Verdict.allow()

    if tool == "notify_carrier":
        if not ctx.tools.fault_rows(ticket_id=action.get("ticket_id")):
            return Verdict.deny("không có lỗi hãng nào được ghi cho ticket này thì không báo hãng")
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of) or {}
        allowed = set(policy.get("carrier_notice_fields") or [])
        payload = action.get("payload") or {}
        extra = sorted(set(payload) - allowed)
        if extra:
            return Verdict.modify("chỉ gửi hãng các trường chính sách cho phép (không gửi dữ liệu cá nhân)",
                                  payload={k: v for k, v in payload.items() if k in allowed})
        return Verdict.allow()

    return Verdict.allow()
