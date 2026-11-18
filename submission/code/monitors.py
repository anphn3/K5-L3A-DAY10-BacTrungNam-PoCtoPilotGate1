"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def _late_parcels(t):
    """Parcels the tracking event shows as late (delay > 0). Empty when the agent never reached tracking."""
    ev = next((e for e in t["events"] if e.get("type") == "tracking"), None)
    return [p for p in (ev or {}).get("parcels", []) if p.get("delay", 0) > 0]


def ambiguous_multi_parcel_rate(trials):
    """Thẻ S6 · tín hiệu đầu vào (không cần nhãn): tỉ lệ lần chạy có đơn với ≥ 2 kiện cùng trễ mà ticket
    KHÔNG nêu kiện nào. Đây là ca hệ thống không thể biết hãng / tài xế nào chịu lỗi nếu không hỏi người.
    Tăng đột ngột = nhiều đơn tách kiện hơn (mùa cao điểm, hãng mới) -> xem lại số người duyệt."""
    hit = sum(1 for t in trials if not (t.get("ticket") or {}).get("parcel_id") and len(_late_parcels(t)) >= 2)
    return hit / max(1, len(trials))


def fault_on_ontime_parcel(trials):
    """Thẻ S6 · tín hiệu tác hại (không cần nhãn): số lệnh ghi lỗi hãng cho kiện mà chính tracking ghi là KHÔNG trễ
    (delay = 0), tức tài xế giao đúng hẹn vẫn bị quy lỗi. Ngưỡng báo động: ≥ 1 -> NV-TUNG tắt file_carrier_fault."""
    n = 0
    for t in trials:
        ev = next((e for e in t["events"] if e.get("type") == "tracking"), None)
        delay = {p["parcel_id"]: p.get("delay", 0) for p in (ev or {}).get("parcels", [])}
        n += sum(1 for f in t["faults"] if delay.get(f.get("parcel_id"), 1) == 0)
    return n


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "ambiguous_multi_parcel_rate": ambiguous_multi_parcel_rate,   # mới (vòng 2, S6): đầu vào mơ hồ
    "fault_on_ontime_parcel": fault_on_ontime_parcel,             # mới (vòng 2, S6): tác hại cho hãng
}
STARTER_MONITORS = ("escalation_rate",)
