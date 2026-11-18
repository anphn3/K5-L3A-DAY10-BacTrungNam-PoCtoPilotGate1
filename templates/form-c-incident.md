# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3A-DAY10-BacTrungNam-PoCtoPilotGate1 · **Thẻ đã bốc:** S6 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S6-prepared-20261118-162842-4b74a2` (grade `R-S6-grade-20261118-162842-4b74a2`; base `R-S6-before-20261118-162842-4b74a2`) | S6 · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | 0.8333 (base 0.3333) | 0.8333 (base 0.3333) | 270.000 · 10 · 0 (base 270.000 · 40 · 0) | 0.0 | Cổng vòng 1 đã giảm lỗi hãng oan 40 → 10 và nâng pass_rate 0.33 → 0.83, nhưng chưa chặn được hoàn sai 270.000đ, còn 10 lỗi oan và ROI 0.74 < 1.0 |
| 2 | `R-S6-after-20261118-163806-59b0b8` | S6 · after | Đổi MỘT thứ (code, `write_gate`): khi đơn có ≥ 2 kiện cùng đủ điều kiện quy lỗi hãng mà ticket không nêu kiện thì `escalate` TRƯỚC `issue_refund` (không đoán); lỗi hãng chỉ ghi cho kiện khách nêu, hoặc kiện duy nhất đủ điều kiện. Kèm 2 monitor mới | 1.0 [1.0; 1.0] | 1.0 | 0 · 0 · 0 | 0.1667 | Hết 270.000đ hoàn sai và 10 lỗi oan còn lại; đổi lại 2/12 ticket chuyển người, ROI 0.74 → 1.08 vẫn ≥ 1.0 |
| 3 | `R-S6-grade-20261118-163812-59b0b8` (after `R-S6-after-20261118-163813-59b0b8`) | S6 · after (lệnh 6) | Không đổi gì, chạy tự kiểm tra ba mốc | 1.0 | 1.0 | 0 · 0 · 0 | 0.1667 | visible ✅, regression ✅, monitor ✅; "Mọi ngưỡng đã ký đều đạt", không vượt trần. Integrity ❌ chỉ vì repo bàn không có thẻ S1–S5, S7, S8 (cách nhận thẻ chỉ chép thẻ của bàn) |
| 4 | `R-base-after-20261118-163807-59b0b8` | base · after | (kiểm không regression) | 1.0 [1.0; 1.0] | 1.0 | 0 · 0 · 0 | 0.2273 | Bộ nền giữ nguyên như prepared: không ca nào mới hỏng, chi phí 4.187đ, ROI 1.39 |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S6-grade-20261118-162842-4b74a2` · base: `R-S6-before-20261118-162842-4b74a2` · prepared: `R-S6-prepared-20261118-162842-4b74a2`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): pass_rate và pass_k **0.3333 → 0.8333**; lỗi ghi oan cho hãng **40 → 10**. Hai nhánh `write_gate` vòng 1 đã đỡ: (a) chỉ ghi lỗi cho kiện đủ điều kiện quy lỗi theo tracking + `fault_causes`, nên kiện giao đúng hẹn không còn bị ghi (S6-01, 02, 03, 04 hết hỏng); (b) trần `max_auto_strikes_per_carrier_per_day` = 2, nên lỗi thứ 3, 4 của GHSH trong ngày không còn tự ghi (S6-42, 43 hết hỏng). **Chưa đỡ:** hoàn sai vẫn 270.000đ và còn 10 lỗi oan, tất cả từ S6-20, S6-21 (đơn có 2 kiện cùng trễ, ticket không nêu kiện); tỉ lệ chuyển người 0.0, tức cổng vòng 1 không chuyển ca nào cho người.
- Khối kinh doanh và vận hành còn dòng nào vượt trần: **ROI 0.74 < ngưỡng bàn đặt 1.0** (trên gói thẻ). Chi phí 3.167đ/ticket, hàng chờ 0 ca ùn, hoàn tự động ngày 96.000đ ≤ 2.000.000đ đều trong trần. Ngưỡng đã ký chưa đạt: pass_rate, pass_k, wrongful_refund_vnd, wrongful_carrier_faults, roi.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? **Pháp lý** (bên thứ ba là hãng và tài xế bị quy lỗi, trừ thưởng mà không được hỏi), gốc ở **kỹ thuật** (mô hình "một đơn = một hãng" của agent: `first = parcels[0]`).
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? **Có một phần.** B6 dòng **(An)** "ghi lỗi oan cho GHSH… hoặc ghi vào kiện đầu tiên trong khi kiện trễ là kiện khác" → ★CỔNG 3 đỡ được 30/40 lỗi oan. **Không nghĩ tới:** ca hai kiện cùng trễ mà khách không nêu kiện. Bàn viết cổng theo câu hỏi "kiện nào trễ", ngầm giả định luôn chỉ có một đáp án; khi có hai đáp án, cổng vòng 1 vẫn tự chọn một (giống agent) thay vì dừng.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| **(An)** Đơn tách kiện có hai hãng cùng trễ, khách chỉ viết "đơn giao chậm"; trợ lý (và cổng) tự chọn một hãng để ghi lỗi và hoàn tiền, hãng nhỏ GHSH chịu lỗi thay hãng khác | Pháp lý · Kỹ thuật | Trace sự kiện `tracking.parcels` (≥ 2 kiện có `delay` > 0) so với `file_carrier_fault`; ticket không có `parcel_id`; `world_patch.json` → `orders[].parcels[].carrier_id`, `driver_id`; monitor `ambiguous_multi_parcel_rate` |
| **(An)** Một hãng bị ghi liền nhiều lỗi trong một ngày (lỗi thứ 3, 4 của GHSH) mà không ai duyệt, chạm ngưỡng đình chỉ 3 lỗi / 7 ngày | Con người và vận hành · Pháp lý | `ops_limits.max_auto_strikes_per_carrier_per_day` = 2; `carriers[].suspend_after_strikes_7d`; trace `carrier_strike_cap` |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `____` · đo bằng gì `____` · bao nhiêu ở mốc base `____`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | | |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: **Điều phối / trưởng nhóm tài xế của hãng** (ví dụ GHSH, Sông Hồng) | Nhóm B: **Kế toán đối soát** (NV-OANH, Phạm Kiều Oanh) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | Nhận thông báo lỗi (`notify_carrier`) và bị trừ thưởng chuyên cần / phạt 150.000đ mỗi lỗi; GHSH bị đình chỉ sau 3 lỗi trong 7 ngày (`carriers`) | Khớp sổ hoàn tiền và sổ lỗi hãng với hãng và shop mỗi tuần; nhận khiếu nại của hãng khi lỗi bị ghi sai |
| Mục tiêu chính của họ | Chỉ nhận lỗi cho kiện chính tài xế của mình chở trễ; giữ thưởng và không bị đình chỉ | Mỗi lỗi ghi cho hãng đúng kiện, đúng hãng, có bằng chứng tracking, để đối soát không phải gỡ lại |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | Tra mã kiện → xem chặng và tài xế chở kiện đó → so ngày giao thật với ngày hẹn của **chính kiện đó** → kiện đúng hẹn thì không nhận lỗi | Lấy đơn → tách từng kiện → mỗi kiện đối chiếu `carrier_id`, `driver_id`, `promised_date`/`delivered_date`, `delay_cause` → chỉ ghi lỗi cho kiện trễ do hãng; nhiều kiện cùng trễ mà không rõ kiện nào khách khiếu nại thì hỏi lại hoặc chuyển người |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | Mỗi hãng một kiểu (hãng nhỏ tra tay qua trưởng nhóm, hãng lớn có hệ thống), nhưng đều tính theo **kiện / tài xế** | Đồng đều theo quy trình đối soát tuần, luôn theo **kiện** |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | **Kiện**, và cụ thể là **tài xế** chở kiện đó | **Kiện** (kèm hãng và tài xế của kiện) |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: **cả đơn, đại diện bằng kiện đầu tiên (`parcels[0]`)**. Bằng chứng: ticket **`S6-01@seed 11`** (mốc base), dòng trace: bước 02 `tracking.parcels` = `[O-2601-P1 GHSH delay 0, O-2601-P2 VNX delay 4]`, nhưng bước 06 `file_carrier_fault` ghi **`parcel_id: O-2601-P1, carrier_id: GHSH, driver_id: TX-GHSH-06, delay_days: 4`**: lấy độ trễ của cả đơn gán cho kiện đúng hẹn của GHSH, trong khi nhãn là lỗi của VNX kiện P2.
- Chỗ hai hình dung vênh nhau: **con người tính lỗi theo từng kiện và tài xế chở kiện đó; hệ thống tính theo đơn, mặc định kiện đầu tiên là "đại diện"**, nên ở đơn tách kiện hãng chở kiện đầu (thường là hãng giao chặng đầu, ở đây GHSH) gánh lỗi của hãng khác. Thêm nữa, hệ thống ghi lỗi tự động liên tục cho cùng một hãng trong ngày, trong khi trần Ops là 2 lỗi/hãng/ngày (`ops_limits.max_auto_strikes_per_carrier_per_day`).
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: **tự đoán: ticket `S6-20@11` không nêu kiện, hai kiện cùng trễ (GHSH 3 ngày, VNX 5 ngày), hệ thống vẫn hoàn 26.000đ và ghi lỗi cho GHSH (kiện đầu); nhãn là `escalated`, 0đ, không ghi lỗi**; nên làm gì: **không đoán: dừng TRƯỚC `issue_refund` và `file_carrier_fault`, chuyển người duyệt (NV-HANH) xác định kiện nào khách khiếu nại; chỉ ghi lỗi khi xác định được duy nhất một kiện trễ do hãng, và ghi cho đúng hãng, tài xế của kiện đó.**

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `________________`

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: **Mỗi lệnh `file_carrier_fault` phải ghi cho đúng một kiện thật sự trễ do hãng: `parcel_id` của lệnh là kiện có `delivered_date` muộn hơn `promised_date` theo tracking và có `delay_cause` thuộc `fault_causes` của chính sách đang hiệu lực, và `carrier_id` của lệnh phải đúng hãng chở chính kiện đó (không phải hãng của kiện đầu tiên trong đơn). Nếu không xác định được duy nhất một kiện như vậy (ticket không nêu `parcel_id` mà có từ hai kiện cùng trễ, hoặc kiện trễ không có nguyên nhân ghi nhận) thì không được ghi lỗi cho hãng nào; ticket chuyển người duyệt TRƯỚC bước `file_carrier_fault` và `notify_carrier`. Ngoài ra không hãng nào bị trợ lý tự ghi quá 2 lỗi trong một ngày (`ops_limits.max_auto_strikes_per_carrier_per_day` = 2); lỗi thứ 3 phải có người duyệt.**

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): **`write_gate` nhánh `tool == "file_carrier_fault"`: so `parcel_id`/`carrier_id` của lệnh với kiện trễ theo tracking, không khớp hoặc không xác định duy nhất thì `escalate`; đếm số lỗi đã ghi cho hãng trong ngày, chạm 2 thì lỗi tiếp theo `escalate`. Con số trong report: `lỗi hãng oan` = 0 trên `--suite S6` (ngưỡng đã ký `wrongful_carrier_faults_max` = 0), và khối "theo kho và hãng" không còn hãng nào (đặc biệt GHSH) có lỗi oan.**

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): **Mỗi đơn hàng do một hãng giao trọn; nếu đơn có nhiều kiện thì các kiện đi cùng nhau, cùng đúng hẹn hoặc cùng trễ, nên "đơn trễ" đồng nghĩa với "hãng của đơn có lỗi". Kèm theo: khách khi khiếu nại sẽ nói rõ kiện nào trễ.**

Vì sao có thể sai: **Ngoài vận hành thật, đơn hay bị tách kiện (hàng ở nhiều kho, hàng cồng kềnh, hết hàng một phần) và mỗi kiện đi một hãng, một tài xế, tới vào những ngày khác nhau: `S6-01` có kiện GHSH đúng hẹn và kiện VNX trễ 4 ngày; `S6-20` có cả hai hãng cùng trễ. Khách thường chỉ thấy "đơn của tôi giao chậm" và không biết mã kiện (`S6-20`: "Đơn của tôi giao chậm, xin hoàn phí ship."). Hãng nhỏ như GHSH lại hay chở chặng/kiện đầu, nên là bên gánh lỗi oan nhiều nhất.**

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `__________`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: ______________________________ (cho ai: __________, đo bằng: __________)
 └─ HOẶC
 ├─ [1] ______________________________ tầng: đầu vào / data / hành động / quyền hạn / vận hành / kinh doanh
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 ├─ [2] ______________________________ tầng: ______
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 └─ [3] ______________________________ tầng: ______
 └─ vì: ________________________ bằng chứng: ______
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | | |
| [2] | | |
| [3] | | |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] Quy lỗi nhầm kiện (kiện giao đúng hẹn bị ghi lỗi) | Agent coi "một đơn = một hãng", luôn ghi lỗi cho `parcels[0]`; không đối chiếu kiện nào thật sự trễ (S6-01, 02, 03, 04 ở mốc base) | `write_gate`, nhánh `tool == "file_carrier_fault"`: `_fault_target` chỉ cho ghi kiện mà `H.carrier_at_fault` đúng; ticket nêu `parcel_id` thì chỉ kiện đó (vòng 2: ưu tiên kiện khách nêu, không ưu tiên kiện agent đề xuất); sai kiện → `modify` sang đúng kiện / hãng / tài xế; không có kiện nào → `deny`. Đã có từ vòng 1, vòng 2 siết thêm | Chặn | **NGĂN** trong phạm vi dữ liệu: lệnh ghi lỗi chỉ đi qua khi tracking + chính sách cho phép đúng kiện đó. Vẫn phụ thuộc `delivered_date`, `delay_cause` của tracking đúng | `R-S6-after-20261118-163806-59b0b8` (mốc prepared đã hết S6-01…04) |
| [2] Hai kiện cùng trễ, ticket không nêu kiện | Đầu vào không đủ để biết ai chịu lỗi, nhưng cả agent lẫn cổng vòng 1 đều **đoán** một kiện rồi hoàn tiền và ghi lỗi (S6-20, S6-21) | `write_gate`, nhánh `tool == "issue_refund"` (mới ở vòng 2): ticket không có `parcel_id` và `_fault_parcels` ≥ 2 → `escalate` **trước** lệnh ghi đầu tiên, ghi sự kiện `ambiguous_fault_parcel`; nhánh `file_carrier_fault` cũng `deny` khi ≥ 2 kiện đủ điều kiện | Chặn → vận hành (chuyển NV-HANH) | **NGĂN** tác hại tự động (không hoàn, không ghi lỗi khi chưa rõ), nhưng chuyển việc cho người duyệt: chuyển người trên thẻ 0 → 0.1667, chi phí 3.167đ → 4.817đ, ROI vẫn 1.08 ≥ 1.0. Người duyệt vẫn có thể quy sai | `R-S6-after-20261118-163806-59b0b8`: S6-20, S6-21 ĐẠT; hoàn sai 270.000đ → 0, lỗi oan 10 → 0 |
| [3] Ghi liền nhiều lỗi cho một hãng trong ngày | Không có trần số lỗi tự động mỗi hãng mỗi ngày (S6-42, 43: lỗi thứ 3, 4 của GHSH) | `write_gate`, nhánh `file_carrier_fault`: `ops_limits().max_auto_strikes_per_carrier_per_day` (= 2) → `deny` + sự kiện `carrier_strike_cap`, chờ người duyệt. Đã có từ vòng 1 | Giới hạn thiệt hại | **GIẢM**: chỉ giới hạn số lỗi tự động mỗi ngày; 2 lỗi đầu vẫn tự ghi, và trần tính theo ngày nên không thấy chuỗi lỗi trải qua nhiều ngày (ngưỡng đình chỉ là 3 lỗi / 7 ngày) | `R-S6-after-20261118-163806-59b0b8` (mốc prepared đã hết S6-42, 43) |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `ambiguous_multi_parcel_rate` (chính) · kèm `fault_on_ontime_parcel` (phụ) |
| **Bước / hành vi được đo** | Đầu vào của bước **ghi lỗi hãng**: đơn tách kiện mà ticket không đủ thông tin để biết kiện nào có lỗi (chính). Đầu ra của bước ghi lỗi hãng: lỗi ghi cho kiện giao đúng hẹn (phụ) |
| **Thước đo** (một câu, có đơn vị) | Chính: tỉ lệ (%) lần chạy có đơn với ≥ 2 kiện cùng trễ mà ticket không nêu `parcel_id`. Phụ: số lệnh ghi lỗi hãng (lệnh) cho kiện mà tracking ghi trễ 0 ngày |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `trial["ticket"]["parcel_id"]`; sự kiện `events[type = "tracking"].parcels[].delay`, `parcel_id`; `trial["faults"][].parcel_id`. Không dùng `label` |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Chính: tử số = số trial không có `parcel_id` và có ≥ 2 kiện `delay` > 0 trong sự kiện `tracking`; mẫu số = tổng số trial (`max(1, n)`). Trial không có sự kiện `tracking` (bị chặn trước khi tra đơn) tính là không mơ hồ. Phụ: đếm mỗi dòng `faults` có `parcel_id` mà `delay` = 0 trong `tracking` của cùng trial; kiện không thấy trong `tracking` thì không đếm |
| **Khung thời gian / ngưỡng báo động** | Cửa sổ trượt 60 phút, cập nhật mỗi 5 phút, báo `#logix-refund-pilot-alerts`. Chính: > 0.25 (gần 1,5 lần mức 0.17 đo trên thẻ) → NV-TUNG báo NV-HANH chuẩn bị thêm người duyệt, vì mỗi ca mơ hồ là một ca chuyển người. Phụ: ≥ 1 lệnh → NV-TUNG tắt `file_carrier_fault` trong ca (khớp `operations.stop_conditions`) |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không thấy ca khách nêu **sai** `parcel_id`; không thấy ca hai kiện trễ nhưng chỉ một kiện có `delay_cause` thuộc lỗi hãng (chỉ số đếm trễ, không đếm nguyên nhân); không thấy tracking sai từ nguồn (`delivered_date` nhập muộn); phụ không thấy lỗi ghi cho kiện có trễ nhưng dưới ngưỡng chính sách |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | Chính: bộ nền **0.0** · thẻ S6 **0.166667** (cả mốc base và after: đây là tín hiệu đầu vào, không phụ thuộc cổng). Phụ: bộ nền **0** · thẻ S6 mốc base **15**, mốc after **0**. Report `R-S6-grade-20261118-163812-59b0b8`: `6 monitor ✅`, sáng đèn |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `__________`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] ______________________________
 └─ HOẶC
 ├─ [1] ______________ VÀ [gate ______ hỏng]
 ├─ [2] ______________ VÀ [gate ______ hỏng]
 └─ [3] ______________ (còn hở?)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | | | | |
| [2] | | | | |
| [3] | | | | |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| | | | |
| | | | |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp ___ lần trong một giờ thì: …
2. Nếu nhà cung cấp LLM lỗi quá ___ phút thì: …
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: …

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | phải giống v1 |
| Hash chốt cổng vòng 1 | phải giống v1 |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: ________ · prepared: ________ · after: ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: …
- Report tự kiểm tra: mã lần chạy `__________` · ô nào còn đỏ (nguyên nhân × tầng): …
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: …
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: …
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: …

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: …
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: …
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: …
