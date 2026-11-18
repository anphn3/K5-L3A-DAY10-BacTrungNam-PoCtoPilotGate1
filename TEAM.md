# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): BacTrungNam
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-BacTrungNam-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Phan Bá An | 2A202603375 | Kỹ sư cổng | ✓ |
|   2 | Nguyễn Thùy Dương | 2A202603388 | Kỹ sư cổng |             |
|   3 | Trần Thị Lý |2A202603404      | Sản phẩm và kinh doanh |             |
|   4 | Phí Hoàng Nam | 2A202603435     | Vận hành và pháp lý |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## PhanBaAn-2A202603375

### Phần việc phụ trách

Trưởng nhóm, Kỹ sư cổng A (P1), theo phân công trong `TASKS.md`:

- Tạo repo, mời thành viên và team chấm, chia việc (`TASKS.md`), điền bảng thành viên.
- Câu 1.3 (Phiếu A, A2 cột Offline) và câu 1.5 (A3). Soát `config/acceptance_criteria.json`, ký và push (A5).
- Máy chạy lệnh duy nhất của bàn: `eval`, `gate`, `checkpoint`, `grade`, `check_submission` (B0, B1, B8, C0, C7).
- Câu 2.6 (B7.1): `write_gate` trong `lab10/guards.py`. Vòng 2: sửa cổng code cùng Dương.
- Câu 2.5 (B6): hai lý do pre-mortem đánh dấu **(An)** (fail-open và ghi hoàn trùng khi LLM lỗi 429; ghi lỗi oan cho hãng).

### Đóng góp cụ thể

- Thiết kế offline metric cho bước ghi lỗi hãng (câu 1.3), dựa trên sự kiện `file_carrier_fault`, `tracking` và nhãn `label.faults`.
- Phát hiện và sửa lỗi xuống dòng CRLF trên máy chạy lệnh (`core.autocrlf`), lỗi này làm cả 19 file bị khoá lệch hash so với `lab10/MANIFEST.json`.
- Ký tiêu chí, chạy mọi lệnh đo của bàn (base, after, prepared, chốt vòng 1, grade S6, gom bài).
- Vòng 1: `write_gate` (tính lại tiền hoàn, lỗi hãng, payload báo hãng từ nguồn sự thật): bộ nền 0.9909 → 1.0, hoàn sai 20.000đ → 0, lỗi oan 1 → 0.
- Vòng 2 (thẻ S6): `write_gate` không đoán kiện khi ≥ 2 kiện cùng đủ điều kiện quy lỗi; 2 monitor `ambiguous_multi_parcel_rate`, `fault_on_ontime_parcel`. Gói S6: lỗi oan 40 → 10 → 0, hoàn sai 270.000đ → 0, ROI 0.74 → 1.08.
- Phiếu: A2 (1.3), A3 (1.5), A5, B0, B1, B6 (2 dòng **(An)**), B7.1 cổng 2–3, B8 phần số liệu, C0, C1, C7, C8, mục "Hạn chế và khó khăn" cuối Phiếu C.

### Khó khăn

- **Repo bàn chỉ có thẻ S6, thiếu S1–S5, S7, S8.** Thẻ phát qua repo thẻ riêng, README repo đó và luật 6 chỉ cho lấy thẻ của bàn mình; link repo thẻ đóng sau giờ phát. Vì `lab10/MANIFEST.json` liệt kê đủ 8 thẻ, lệnh 6 trên máy bàn luôn báo `1 integrity ❌` do **thiếu file** (không phải bị sửa). 4 file S6 đã kiểm khớp hash trước khi chép. Đã ghi ở Phiếu C mục "Hạn chế và khó khăn" và báo Lab Coach.
- Mạng tới GitHub chập chờn, nhiều lần phải push lại.

### Dùng AI

Dùng Claude (Claude Code) để: đọc README và code, soạn nháp phân công (`TASKS.md`), câu 1.3, câu 1.5, bản nháp tiêu chí và câu tiêu chí A4, bản nháp pre-mortem B6, viết và kiểm thử `write_gate` vòng 1 và 2, viết 2 monitor, dò trace S6, điền C0/C1/C7/C8, kịch bản demo (`DEMO.md`), kiểm `submission.json`. Mọi ngưỡng và quyết định do cả bàn đọc lại và chốt.

### Bằng chứng

- Commit: ký tiêu chí `bcd0a06`; `write_gate` vòng 1 `3675755`; chốt vòng 1 `8cd3e01` (hash `7365d885`); nhận thẻ `661635b`; vòng 2 S6 `cee788c`; bài nộp `1899a58`.
- Mã lần chạy: base `R-base-before-20261118-154922-e115de` · after `R-base-after-20261118-160208-4b74a2` · prepared `R-base-prepared-20261118-161233-4b74a2` · S6 after `R-S6-after-20261118-163806-59b0b8` · grade `R-S6-grade-20261118-163815-59b0b8`.

### Exit ticket

- **Học được:** Tôi nhận ra rằng thêm một lớp kiểm soát (guard) không đồng nghĩa với việc hệ thống đã an toàn. Cụ thể, ở thẻ S6, cổng vòng 1 đã ngăn được 30/40 lỗi oan nhưng vẫn tự đưa ra phán đoán khi có hai kiện hàng cùng trễ. Khi dữ liệu chưa đủ để kết luận, hệ thống nên chuyển cho con người xử lý thay vì cố gắng đoán.
- **Chưa chắc:** Nếu dữ liệu tracking từ hãng vận chuyển không chính xác, liệu các guard và monitoring hiện tại có đủ khả năng phát hiện lỗi và ngăn hệ thống quy trách nhiệm oan cho hãng không, vì hôm nay chúng tôi chưa kiểm chứng với dữ liệu thực tế có sai lệch từ phía carrier.

## NguyenThuyDuong-2A202603388

### Phần việc phụ trách

Kỹ sư cổng B (P2), theo phân công trong `TASKS.md`:

- Phối hợp câu 1.3–1.5 (Phiếu A, A2–A3).
- Câu 2.2 (B2): đọc trace và soát lỗi; câu 2.6–2.8 (B7.1–B7.3): `pre_guard` trong `lab10/guards.py`, tránh rò rỉ dữ liệu và hai ticket hiểm.
- Vòng 2: phân tích lỗi C2–C3, fault tree C6/C9, phối hợp sửa cổng C7 và thêm chỉ số theo dõi trong `lab10/monitors.py` (C8).
- Demo: giải thích cổng code và chỉ số theo dõi.

### Đóng góp cụ thể

- Bổ sung telemetry production ở Phiếu A câu 1.4: phát hiện lệnh ghi lỗi hãng thiếu căn cứ, xác định dữ liệu không cần nhãn, công thức, điểm mù và đề xuất ngưỡng cảnh báo để nhóm thống nhất.
- Phân tích `T-002@55` ở B2: tìm bước `model_override` dùng lời khách khai 5 ngày thay tracking 2 ngày, dẫn tới hoàn sai 20.000đ và ghi lỗi oan VNX. Phân biệt lỗi nguồn với hai hậu quả.
- Đóng góp lý do pre-mortem B6 và đề xuất cổng; viết hai bước tránh rò rỉ dữ liệu đánh giá ở B7.2, tách kết quả trên bộ dùng để sửa khỏi bằng chứng đánh giá độc lập.
- Xây dựng `pre_guard` vòng 1: chuẩn hóa yêu cầu giao trễ theo tracking; chuyển yêu cầu giao trễ có ghi chú checkout tự do sang người trước khi LLM đọc. Phối hợp với `write_gate` của An; ghi rõ rủi ro tăng hàng chờ và giới hạn nhận diện ngôn ngữ.
- Viết tính chất và hai ticket hiểm B7.3, chạy trace: khai trễ 19 ngày trên đơn DB trễ 2 ngày không được hoàn; chỉ thị bỏ qua chính sách không làm hoàn toàn bộ tiền hàng, chỉ hoàn đúng phí ship 25.000đ. Kiểm tra thêm ghi chú checkout bằng world sao chép trong bộ nhớ; chạy 13 test công khai, tất cả OK.
- Với S6, phân tích trace base/prepared, điền C2 và C3.2; xây dựng fault tree C6/C9 với ba nhánh: quy nhầm kiện, tự đoán khi nhiều kiện cùng đủ điều kiện, tích lũy lỗi vượt trần. Nêu rõ prepared đã chặn nhánh A/C, vòng 2 xử lý B trước khi ghi tiền, và rủi ro còn lại ở nguồn tracking, người duyệt, tích lũy nhiều ngày.
- Đã rà soát phần phân tích với nhóm. Bản sửa `write_gate` vòng 2 và hai monitor do An triển khai; số liệu eval/grade do An chạy trên máy chính, em dẫn lại trong phiếu và không nhận là phần code hoặc lần chạy của mình.

### Dùng AI

Dùng ChatGPT/Codex hỗ trợ đọc đề/code, viết và sửa `pre_guard`, chạy test/trace, soạn các mục phiếu được giao và thao tác Git. Em đã rà soát nội dung; ngưỡng và quyết định cuối cùng do nhóm thống nhất.

### Bằng chứng

- `b68b00c`: thông tin cá nhân và telemetry câu 1.4 trong Phiếu A.
- `05b9230`: B2, phân tích trace `T-002@55`.
- `63b8efd`: B6 và B7.2, gộp đóng góp với phần của nhóm.
- `24a42bc`: `pre_guard`, B7.1/B7.3 và kết quả hai ticket `ADHOC-1@55` (`O-1002`) / `ADHOC-1@11` (`O-1001`); 13 test công khai OK tại thời điểm kiểm.
- `27143bb`: C2, C3.2, C6, C9. Trace base: `S6-01@11`, `S6-20@11`, `S6-42@11`; trace prepared đã đối chiếu: `S6-01`, `S6-04`, `S6-20`, `S6-21`, `S6-43` ở seed 11.
- Report P1 cung cấp để đối chiếu: prepared `R-S6-prepared-20261118-162842-4b74a2`, after `R-S6-after-20261118-163806-59b0b8`. C0 ghi hoàn sai 270.000đ → 0, lỗi oan 10 → 0, pass_rate 0.8333 → 1.0; đây là kết quả chung của hệ thống, không phải tác động riêng của `pre_guard`.

### Exit ticket

- Điều học được: vị trí đặt cổng quan trọng như điều kiện kiểm tra. Với S6-20/S6-21, nếu có nhiều kiện đủ điều kiện mà chưa rõ khách yêu cầu kiện nào thì phải chuyển người trước `issue_refund`; chặn ở `file_carrier_fault` là quá muộn vì tiền đã ghi. Kết quả base, prepared và after giúp phân biệt phần chuẩn bị trước với phần sửa sau sự cố.
- Điều còn chưa chắc: tracking và định danh kiện có đủ chính xác khi pilot thật hay không, và người duyệt có chịu được tải ca mơ hồ tăng lên không. Trần 2 lỗi/hãng/ngày chưa ngăn được tích lũy qua nhiều ngày; cần đo thêm thời gian chờ, chất lượng quyết định của người duyệt và đối soát cửa sổ 7 ngày.

## TranThiLy-2A202603404

### Phần việc phụ trách

Sản phẩm và kinh doanh (P3), theo phân công trong `TASKS.md`:

- Câu 1.1 (Phiếu A, A1): mục tiêu cấp hệ thống (câu 1.2 do Nam viết).
- Câu 1.6 (Phiếu A, A4) và `config/acceptance_criteria.json`: người đứng tên `signed_by`; soát và thống nhất bộ ngưỡng với bàn trước khi P1 ký.
- Câu 2.3 (Phiếu B, B3): bản đồ dữ liệu và ví dụ drift.
- Câu 2.5 (Phiếu B, B6): một lý do pre-mortem đánh dấu **(Lý)**.
- Câu 2.9 (Phiếu B, B7.4): mục `business` của `config/operating_gates.json`.
- B5 checklist: PIC các dòng 2 (Dữ liệu), 6 (Chi phí), 9 (Quyết định).
- B8 quyết định v1 và C12 quyết định v2; demo phần con số và quyết định.

### Đóng góp cụ thể

- Viết mục tiêu cấp hệ thống (câu 1.1): xử lý đúng chính sách hiệu lực, tiền khớp sổ cái, không ghi lỗi oan cho hãng, không lộ dữ liệu, ca không chắc thì chuyển người trong SLA 60 phút.
- Soạn một bộ ngưỡng và `decision_rule`; khi trùng với bản nháp của bàn (`8dc52ac`) thì so sánh hai bản, chọn bản của bàn (`decision_rule` cụ thể hơn) và đối chiếu từng ngưỡng với `data/world.json` để giải thích được khi demo (pass_k 0,95 nghĩa là tối đa 1/22 ticket chập chờn; ROI 1,0 phải bù phí giữ chỗ người trực 30.000đ/ca).
- Bản đồ dữ liệu (B3): xác định tracking (`delivered_date`, `delay_cause`) là nguồn sự thật, số ngày khách khai là bản sao không tin được; ví dụ drift là **quan hệ vào–ra đổi**: REFUND-v3 → REFUND-v4 ngày 2026-12-01 (hạn mức 200.000đ → 100.000đ, trễ do bão không còn là lỗi hãng).
- Cổng kinh doanh (B7.4): `daily_refund_cap_vnd` 2.000.000đ (ngân sách Finance), `cost_budget_per_ticket_vnd` 1.500đ (trần LLM), `pilot_scope` all 100%, `roi_min` 1,0; đối chiếu với số base (chi phí 4.203đ/ticket, ROI 1,34; nhóm ticket không xác định kho 10.359đ/ticket, đắt hơn làm tay).
- Pre-mortem (B6): thêm lý do drift chính sách v4 (lăng kính Kinh doanh), đưa vào Risk register và đặt ngày quyết định lại trước 2026-11-30.
- Nhận ra chỉ số an toàn ở base trượt nhưng **chưa áp được "Dừng"** vì `decision_rule` ghi "sau khi đã sửa"; quyết định v1 phải dựa trên mốc prepared.

### Dùng AI

Dùng Claude để: đọc đề và `data/world.json`, lập checklist việc của P3, soạn nháp câu 1.1, bản đồ dữ liệu B3, lý do cho các con số B7.4, lý do pre-mortem B6, nháp B8; hướng dẫn xử lý conflict Git. Em tự đối chiếu mọi con số với `data/world.json` và report của P1 (mã lần chạy base), và chỉ đưa vào phiếu những gì em giải thích được. Ngưỡng tiêu chí do cả bàn chốt.

### Bằng chứng

- Commit: `f5f5251` (B3 bản đồ dữ liệu + drift), `27a39dd` (B7.4 + `operating_gates.json` mục `business`), `55c676e` (A1 câu 1.1, MSSV), `fab6f76` (B7.4 đối chiếu số base), commit B6 thêm lý do drift v4.
- Tiêu chí ký: commit `bcd0a06` (`Sign acceptance criteria`), hash tiêu chí `8433f76d`, `signed_by` Trần Thị Lý.
- Lần chạy dùng để đối chiếu: `R-base-before-20261118-154922-e115de`.
- Phiếu: A mục A1; B mục B3, B5 (dòng 2, 6, 9), B6 (dòng **(Lý)**), B7.4, B8; C mục C5, C12 *(điền tiếp ở vòng 2)*.

### Exit ticket

*(điền cuối buổi)*

## PhiHoangNam-2A202603435

### Phần việc phụ trách

Vận hành và pháp lý (P4), theo phân công trong `TASKS.md`:

- Phiếu A: câu 1.2 (A1, mục tiêu nhìn từ chị Oanh và chị Hạnh); câu 1.4 (A2, cột Telemetry production, bàn chốt dùng bản của Dương); A4 bước 2 (soát bốn câu hỏi), soát chéo ngưỡng với Lý trước khi ký.
- Phiếu B: câu 2.4 (B4 HAZOP vòng 1 trên `notify_carrier`, B5 checklist 9 nhóm); một lý do pre-mortem **(Nam)** ở B6; câu 2.10 (B7.5 Runbook phần 1–3, B7.6 Giờ cao điểm).
- `config/operating_gates.json`: mục `operations` (`pic`, `approver_id`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`, `stop_conditions`, `alert_channel`) và mục `legal`.
- Vòng 2: bốc thẻ, C4 (HAZOP của thẻ), C10 (risk register), C11 (checklist, Runbook phần 4–5), điền `submission/submission.json`.
- Demo: trả lời phần người trực, runbook, pháp lý.

### Đóng góp cụ thể

- Đặt mọi con số trong `operations` theo `ops_limits` và `ops_facts` đã thống nhất với Ops và Finance: PIC `NV-TUNG` (người giữ công tắc tắt trợ lý), người duyệt `NV-HANH` (khớp `staff_behavior.trust_conditions`), 1 người trực, 6 ca/giờ, chờ tối đa 60 phút (`review_sla_minutes`); bốn điều kiện dừng đều có ngưỡng 1, khớp ba chỉ số an toàn đã ký bằng 0.
- Đọc `lab10/agent.py` và phát hiện thông báo gửi hãng chứa hai trường ngoài `carrier_notice_fields` của chính sách: `customer_note` (nguyên văn chữ khách) và `recipient_contact` (tên, SĐT người nhận quà). Cổng pháp lý lọc theo tên trường cấp ngoài cùng của payload, nên đặt `legal.pii_fields_blocked_to_third_party` = `["customer_note", "recipient_contact"]` thay vì `phone`, `name`. Bật `carrier_fault_requires_recorded_cause`.
- HAZOP B4: tìm nhánh agent luôn lấy hãng của kiện đầu tiên (`parcels[0]`) nên có thể ghi lỗi nhầm hãng ở đơn nhiều kiện, và nhánh đơn quà tặng lộ SĐT người nhận (chưa thấy trên trace `T-002@55`).
- Runbook 2 và Giờ cao điểm dùng số base `R-base-before-20261118-154922-e115de`: tính được nếu xếp cố định 2 người trực thì chi phí khoảng 5.567đ/ticket, vượt ngưỡng 5.000đ đã ký, nên chỉ gọi người thứ hai vào ngày cao điểm thật.
- Soát A4 bước 2: chỉ ra câu ranh giới "200.000đ" phải viết lại khi REFUND-v4 có hiệu lực từ 2026-12-01 (hạn mức tự động còn 100.000đ), và shop chưa có chỉ số riêng khi ghi sai `payer`.

### Dùng AI

Dùng Claude (Claude Code) để: đọc README, đề bài và code (`lab10/agent.py`, `lab10/tools.py`, `lab10/ops.py`) để tra dữ kiện; soạn nháp câu 1.2, câu 1.4, A4 bước 2, HAZOP B4, checklist B5, runbook B7.5–B7.6 và mục `operations`/`legal` trong config; soạn phần giải thích con số để demo. Nam đọc lại, đối chiếu với `data/world.json` và chốt các con số. Các ngưỡng cảnh báo sớm (30 phút, 4 ca, 80% trần), thời hạn dừng 15 phút và tên kênh `#logix-refund-pilot-alerts` là bàn tự chọn, không có trong dữ liệu.

### Bằng chứng

- Commit `5639919`: Phiếu A câu 1.2, câu 1.4; thông tin P4 trong bảng thành viên.
- Commit `2882ecb`: khôi phục cột Telemetry câu 1.4 (bản của Dương) bị mất khi merge.
- Commit `a066507`: A4 bước 2, B4, B5, `config/operating_gates.json` mục `operations` và `legal`, Runbook B7.5–B7.6.
- Commit `c8ce989`: soát Runbook B7.5–B7.6 theo config và số base, cập nhật checklist B5 theo base, lý do **(Nam)** ở B6, mục cá nhân trong `TEAM.md`.
- Commit `c943015`: Phiếu C mục C4 (HAZOP thẻ S6), C10 (risk register), C11 (cập nhật checklist, Runbook phần 4–5); điền `submission/submission.json` (trừ quyết định v2 và ba dòng bắt buộc).
- Lần chạy đối chiếu: `R-base-before-20261118-154922-e115de` (số base dùng trong B5, Runbook 2, B7.6).
- Phiếu: `templates/form-a-criteria.md` (A1 câu 1.2, A4 bước 2); `templates/form-b-evaluation-gates.md` (B4, B5, dòng **(Nam)** ở B6, B7.5, B7.6).

### Exit ticket

- Một điều học được: cổng pháp lý chỉ đúng khi biết chính xác dữ liệu đi ra ngoài trông thế nào. Ghi `phone` vào danh sách chặn nghe đúng nhưng không chặn được gì, vì số điện thoại nằm bên trong trường `recipient_contact`; phải đọc code mới thấy.
- Một điều còn chưa chắc: 1 người trực có đủ khi lượng ticket tăng gấp ba hay không. Ước tính cho thấy vẫn dưới sức 6 ca/giờ, nhưng nếu các ca chuyển người dồn vào cùng một lúc thì hàng chờ có thể vượt 60 phút, và thêm người cố định lại làm chi phí vượt ngưỡng đã ký; cần đo bằng eval khi có thẻ sự cố.
