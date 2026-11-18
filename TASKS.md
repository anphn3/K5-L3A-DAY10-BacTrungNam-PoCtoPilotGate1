# Giao việc · LAB 10 · BacTrungNam

Repo: `K5-L3A-DAY10-BacTrungNam-PoCtoPilotGate1` · Đọc kỹ `README.md` mục 1, 3, 5 trước khi làm.

## 1. Vai

| Mã | Người | Vai | Sở hữu chính |
|---|---|---|---|
| P1 | Phan Bá An (trưởng nhóm) | Kỹ sư cổng A | **Máy chạy lệnh duy nhất**, `write_gate` trong `lab10/guards.py`, gom bài |
| P2 | Nguyễn Thùy Dương | Kỹ sư cổng B | `pre_guard` trong `lab10/guards.py`, `lab10/monitors.py`, trace, ticket hiểm |
| P3 | Trần Thị Lý | Sản phẩm và kinh doanh | `config/acceptance_criteria.json`, mục `business` của `config/operating_gates.json`, quyết định v1/v2 |
| P4 | Phí Hoàng Nam | Vận hành và pháp lý | Mục `operations` + `legal` của `config/operating_gates.json`, HAZOP, checklist, runbook, `submission/submission.json` |

## 2. Năm luật cả nhóm phải nhớ

1. **Chỉ máy P1 chạy** `criteria sign`, `eval`, `gate`, `checkpoint`, `grade`, `check_submission`. Thư mục `runs/` không lên git, nên nhật ký chỉ nằm ở máy nào chạy lệnh. Người khác chỉ chạy `trace` và test trên máy mình.
2. **Ký tiêu chí rồi push trước lần `eval` đầu tiên.** Sau khi ký, không ai mở hay lưu `config/acceptance_criteria.json` nữa. Một dấu cách cũng làm đổi hash.
3. Không sửa file ngoài danh sách ở README mục 1. Sau lệnh `checkpoint`, không đụng vào `*round1*`.
4. Không viết code xử lý riêng theo mã ticket hay câu chữ cụ thể. Không chặn hết. Không thu hẹp phạm vi pilot về 0.
5. Mọi ngưỡng và con số do nhóm tự chọn. Người phụ trách phải giải thích được lúc demo vì sao chọn số đó.

## 3. Việc theo mốc thời gian

### Phút 0–15 · Cài đặt

| Ai | Việc | Xong khi |
|---|---|---|
| P1 | Mời 3 bạn và team chấm (quyền Read) vào repo. Push `TEAM.md` và `TASKS.md` | Cả nhóm thấy repo |
| P2, P3, P4 | `git clone`, `git remote add upstream ...`, `git config user.name "<MSSV mình>"`, `git config user.email "<MSSV mình>@example.com"` | `git remote -v` có `origin` và `upstream` |
| Mọi người | `python -m unittest discover -s tests` | `Ran 13 tests ... OK` |
| P2, P3, P4 | Gửi MSSV cho P1 để điền `TEAM.md` | Bảng đủ MSSV |

### Phút 15–65 · Khối 1, Phiếu A (`templates/form-a-criteria.md`). **Chưa chạy eval.**

| Ai | Câu, mục | File |
|---|---|---|
| **P3** (chính) | 1.1–1.2 (A1), 1.6 (A4: câu "Nếu … thì chúng tôi sẽ …") | `config/acceptance_criteria.json`: `team` = `K5-L3A-DAY10-BacTrungNam-PoCtoPilotGate1`, `signed_by`, `required.*`, `nice_to_have.escalation_rate_max`, `business_ops.*`, `stop_condition`, 4 dòng `decision_rule` |
| P1 + P2 | 1.3–1.4 (A2: bảng thước đo → dữ liệu → cách tính), 1.5 (A3: khoảng tin cậy) | Phiếu A |
| P4 | A4: bốn câu soát, hai câu ranh giới đầu ra. Soát chéo các ngưỡng với P3 | Phiếu A |
| **P1** (phút 60–65) | `python -m lab10.criteria sign`, commit và **push ngay**, rồi điền A5 (giờ ký, mã commit) | Máy in `ĐÃ KÝ.` và push thành công |

### Phút 65–85 · Khối 2A, Phiếu B (`templates/form-b-evaluation-gates.md`). Chưa sửa code hay config.

| Ai | Câu, mục | Lệnh |
|---|---|---|
| P1 | 2.1 → B0 (mã lần chạy), B1 | `eval --suite base --stage base --note "baseline"`, rồi `gate --run runs/<mã>/report.json` |
| P2 | 2.2 → B2 (bảng soát lỗi `T-002@55`) | `trace --suite base --ticket T-002 --seed 55` |
| P3 | 2.3 → B3 (bản đồ dữ liệu, một ví dụ drift) | — |
| P4 | 2.4 → B4 (HAZOP ≥ 3 dòng, trong đó ≥ 2 dòng ngoài kỹ thuật), B5 (checklist 9 nhóm, mỗi dòng **một PIC có tên**) | — |
| Cả nhóm | 2.5 → B6 (pre-mortem 4 lăng kính). Đánh dấu 2–3 lý do sẽ thành cổng | — |

### Phút 85–105 · Khối 2B, dựng cổng

| Ai | Câu, mục | File |
|---|---|---|
| P1 | 2.6 → B7.1 (cổng `write_gate`) | `lab10/guards.py` |
| P2 | 2.6 (cổng `pre_guard`), 2.7 → B7.2 (2 bước tránh rò rỉ dữ liệu), 2.8 → B7.3 (một tính chất và 2 ticket hiểm `--adhoc`) | `lab10/guards.py` |
| P3 | 2.9 → B7.4: `daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope`, `roi_min`. Mỗi số một câu lý do lấy từ `data/world.json` (`ops_limits`, `ops_facts`) | `config/operating_gates.json` mục `business` |
| P4 | 2.10 → B7.5, B7.6: `pic`, `approver_id`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`, `stop_conditions`, `alert_channel`, `legal.*`. Runbook phần 1–3 và mục Giờ cao điểm, khớp với các con số trong config | `config/operating_gates.json` mục `operations`, `legal` |
| P1 | Chạy `eval --suite base --stage after --note "cổng vòng 1: ..."` và test | Không có ca mới hỏng so với base. `operations.pic` không trống |

### Phút 105–115 · Chốt vòng 1 và quyết định v1

| Ai | Việc |
|---|---|
| P1 | `python -m lab10.checkpoint`, `eval --suite base --stage prepared`, `gate --run ...`. Gửi mã lần chạy cho P3 |
| P3 | B8, cột v1: một quyết định, ba bằng chứng có mã lần chạy, dòng `decision_rule`, kho hoặc hãng có số xấu nhất, ngày quyết định lại |
| P1 | Commit và push (lệnh ở cuối B8). Máy phải in `ĐÃ CHỐT cổng vòng 1` |

### Phút 125–200 · Khối 3, Phiếu C (`templates/form-c-incident.md`)

| Ai | Câu, mục | Ghi chú |
|---|---|---|
| P1 | 3.0 → C0, kéo thẻ, chạy `grade` **trước khi sửa** | `git pull --no-rebase --no-edit --allow-unrelated-histories -X ours upstream main`, rồi `python -m lab10.grade --incident Sx` |
| P4 | Đi bốc thẻ. Ghi `Thẻ đã bốc:` ở đầu Phiếu C | Chỉ làm đúng thẻ đã bốc |
| Cả nhóm | C1: cổng vòng 1 đỡ được gì, đối chiếu với pre-mortem | — |
| P2 | 3.1 → C2 (bảng soát lỗi), C3 (phần riêng theo thẻ; thẻ S4 bỏ qua), 3.4 → C6 (fault tree trước khi sửa) | Trace ≥ 2 ticket hỏng theo 2 kiểu khác nhau |
| P4 | C4: HAZOP của thẻ, ≥ 3 dòng | Không ghi đè HAZOP vòng 1 |
| P3 | 3.2–3.3 → C5: specification và giả định môi trường | — |
| P1 + P2 | 3.5 → C7: sửa `guards.py` nếu nguyên nhân là kỹ thuật | Mỗi lần chỉ đổi **một** thứ |
| P3 + P4 | 3.5 → C7: sửa config nếu nguyên nhân là người, tiền hoặc phạm vi (`pilot_scope`, `reviewers_on_shift`, `review_sampling_pct`, `decision_note`, `legal.*`) | — |
| P2 | 3.6 → C8: thêm ≥ 1 hàm chỉ số mới phía trên dict `MONITORS` và đăng ký vào dict (`escalation_rate` có sẵn không tính) | `lab10/monitors.py` |
| P1 | Chạy `eval --suite Sx --stage after`, `eval --suite base --stage after`, `grade --incident Sx` | Có `monitor ✅` và `regression ✅` |
| P2 | 3.7 → C9: fault tree sau khi sửa, có bằng chứng ở lá | — |
| P4 | C10 (≥ 1 dòng risk register), C11 (cập nhật checklist, runbook phần 4–5) | — |
| **P3** | **C12, quyết định v2**: cột v2, mục "Chỉ ở v2", ba dòng bắt buộc gắn con số | **Không chọn "Tiếp tục"** nếu report còn vượt trần hoặc còn ngưỡng chưa đạt |
| P4 | Điền `submission/submission.json`: `team`, `members` dạng `"HoVaTen-MSSV"`, `incident`, `decision_v1`, `decision_v2`, `three_lines` chép từ C12 | `team` giống hệt trong tiêu chí đã ký |
| P1 | `python -m lab10.check_submission --collect`, sửa từng dòng `[THIẾU]` | Dòng cuối in `ĐỦ THÀNH PHẦN` |

### Phút 200–240 · Demo và nộp

| Ai | Việc |
|---|---|
| P1 | Chiếu ba cột `base · prepared · after` |
| P2 | Trả lời phần cổng code và chỉ số theo dõi |
| P3 | Trả lời phần con số và quyết định v2 |
| P4 | Trả lời phần người trực, runbook, pháp lý |
| P1 | Sau demo: trả mọi số đã đổi thử về bản v2, chạy lại lệnh 6 và lệnh 7, rồi push lần cuối |
| **Mọi người** | Viết mục `## HoVaTen-MSSV` của mình trong `TEAM.md` (phần việc, đóng góp, bằng chứng, exit ticket, có dùng AI cho việc gì). **Tự nộp link repo trên LMS** |

## 4. Quy tắc git để tránh conflict

- Luôn chạy `git pull` trước khi sửa. Sửa xong mục nào thì commit và push ngay, mỗi lần một ít.
- Ba phiếu: mỗi người chỉ sửa đúng mục của mình ở bảng trên.
- `lab10/guards.py`: P1 push `write_gate` trước, P2 pull rồi mới push `pre_guard`.
- `config/operating_gates.json`: P3 push mục `business` trước, P4 pull rồi push `operations`/`legal`.
- Commit message nói rõ phần đã làm, ví dụ `Form B: HAZOP B4`.
- Không push lên `upstream`.
