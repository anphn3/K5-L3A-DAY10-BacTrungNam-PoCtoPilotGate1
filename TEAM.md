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

### Dùng AI

Dùng Claude (Claude Code) để: đọc README và code, soạn nháp phân công (`TASKS.md`), câu 1.3, câu 1.5, bản nháp tiêu chí và câu tiêu chí A4, bản nháp pre-mortem B6. Mọi ngưỡng và quyết định do cả bàn đọc lại và chốt.

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu. *(điền dần trong buổi)*

### Exit ticket

*(điền cuối buổi)*

## NguyenThuyDuong-2A202603388

### Phần việc phụ trách

Kỹ sư cổng B (P2), theo phân công trong `TASKS.md`:

- Phối hợp câu 1.3–1.5 (Phiếu A, A2–A3).
- Câu 2.2 (B2): đọc trace và soát lỗi; câu 2.6–2.8 (B7.1–B7.3): `pre_guard` trong `lab10/guards.py`, tránh rò rỉ dữ liệu và hai ticket hiểm.
- Vòng 2: phân tích lỗi C2–C3, fault tree C6/C9, phối hợp sửa cổng C7 và thêm chỉ số theo dõi trong `lab10/monitors.py` (C8).
- Demo: giải thích cổng code và chỉ số theo dõi.

### Đóng góp cụ thể

### Bằng chứng

### Exit ticket

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
- Lần chạy đối chiếu: `R-base-before-20261118-154922-e115de` (số base dùng trong B5, Runbook 2, B7.6).
- Phiếu: `templates/form-a-criteria.md` (A1 câu 1.2, A4 bước 2); `templates/form-b-evaluation-gates.md` (B4, B5, dòng **(Nam)** ở B6, B7.5, B7.6).

### Exit ticket

- Một điều học được: cổng pháp lý chỉ đúng khi biết chính xác dữ liệu đi ra ngoài trông thế nào. Ghi `phone` vào danh sách chặn nghe đúng nhưng không chặn được gì, vì số điện thoại nằm bên trong trường `recipient_contact`; phải đọc code mới thấy.
- Một điều còn chưa chắc: 1 người trực có đủ khi lượng ticket tăng gấp ba hay không. Ước tính cho thấy vẫn dưới sức 6 ca/giờ, nhưng nếu các ca chuyển người dồn vào cùng một lúc thì hàng chờ có thể vượt 60 phút, và thêm người cố định lại làm chi phí vượt ngưỡng đã ký; cần đo bằng eval khi có thẻ sự cố.
