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


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    return Verdict.allow()
