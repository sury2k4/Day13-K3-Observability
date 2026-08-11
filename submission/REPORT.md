# Báo cáo Day 13 Observability

Trạng thái: đã hoàn thành đến Checkpoint 3.

## 1. Thông tin nhóm

- Tên nhóm: Nhóm 3
- Repository URL: https://github.com/sury2k4/Day13-K3-Observability.git
- Commit SHA cuối: 9726a52
- Thành viên và vai trò:
  - Nguyễn Công Hùng - 2A202601071 (Backend - CP1)
  - Hoàng Quang Minh - 2A202601301 (SRE - CP2)
  - Lý Minh Hải - 2A202601503 (QA - CP3 & Report)

## 2. Kết quả kỹ thuật

- Điểm `validate_logs.py`: 100/100 (2 correlation IDs, 0 PII leak)
- Tổng số traces: 20 (10 baseline, 10 candidate)
- Số PII leak còn lại: 0
- Link/đường dẫn dashboard:

## 3. Logging và tracing

- Evidence correlation ID: [logging_pii_checkpoint-1.jsonl](evidence/logging_pii_checkpoint-1.jsonl), `req-abcdef12` và `req-7a7c2ed8`
- Evidence PII redaction: [logging_pii_checkpoint-1.jsonl](evidence/logging_pii_checkpoint-1.jsonl)
- Evidence trace waterfall: [trace_waterfall_checkpoint-2.txt](evidence/trace_waterfall_checkpoint-2.txt)
- Giải thích một span đáng chú ý: generation span có prompt version, model, usage và cost; mở trace `8c97f83e077d33e3b9eae1375f20c1de` để kiểm tra candidate v2.

## 4. Prompt versioning

- Prompt name: `day13-chat`
- Version/label baseline: v1 / `baseline`, `production`
- Version/label candidate: v2 / `candidate`
- Trace ID của mỗi version: [traces_prompt_checkpoint-2.txt](evidence/traces_prompt_checkpoint-2.txt)
- Bằng chứng đổi label hoặc rollback: [prompt_rollback_checkpoint-2.txt](evidence/prompt_rollback_checkpoint-2.txt)

## 5. Dashboard, SLO và alerts

- Kết quả `validate_dashboard.py`: HỢP LỆ: 6/6 panel
- Evidence dashboard: [dashboard_checkpoint-2.txt](evidence/dashboard_checkpoint-2.txt)
- SLO đã chọn và lý do: latency P95 <= 3000 ms, error rate <= 2%, quality >= 0.75; đây là các ngưỡng người dùng cảm nhận được và khớp dashboard contract.
- Alert rules và runbook: `config/alert_rules.yaml`, [docs/alerts.md](../docs/alerts.md)

## 6. Điều tra challenge

- Evidence: [challenge_checkpoint-3.txt](evidence/challenge_checkpoint-3.txt)
- Challenge ID: `day13-k3-observability-v1`
- Triệu chứng từ metrics: latency P50 2650 ms, P95 2992 ms, vượt ngưỡng challenge 2000 ms; error breakdown rỗng.
- Trace ID liên quan: `389e00d5f402473a8202a0e4fbfb7cbc` và `8d041c2baee1316ed24ad81a8ec9b336`
- Log line/correlation ID liên quan: `req-0e75c59b` (2992 ms), `req-1f99cb65` (2651 ms)
- Root cause: `retrieve()` bị incident `rag_slow` chèn `sleep(2.5)`.
- Fix action: tắt incident và xác nhận latency hồi phục 150–155 ms; production fix dùng timeout retrieval và fallback nhanh.
- Preventive measure: alert P95, metric riêng cho retrieval span và load test timeout/fallback.

## 7. Đóng góp cá nhân

Với mỗi thành viên, ghi rõ nhiệm vụ và link commit/PR tương ứng.

| Thành viên | Phần việc | Commit/PR | Điều đã học |
|---|---|---|---|
| Nguyễn Công Hùng (2A202601071) | Backend (CP1): Xây dựng JSONL logging với correlation ID tracking (`x-request-id`), bổ sung metadata API (`user_id_hash`, `session_id`, `feature`, `model`, `env`), xây dựng module redact thông tin nhạy cảm PII (Email, Phone VN, CCCD, Credit Card). | `5e86e2c` (`CP1: logging correlation and PII redaction`) | Hiểu rõ cơ chế `structlog` & contextvars trong FastAPI, kỹ năng redaction PII tự động trước khi ghi log. |
| Hoàng Quang Minh (2A202601301) | SRE (CP2): Cấu hình OpenTelemetry / Langfuse tracing, prompt versioning (v1/v2, baseline/candidate/production, rollback), thiết lập dashboard yaml & alert rules (`config/alert_rules.yaml`, `docs/alerts.md`). | `ff60bfa` / `2130af7` (`checkpoint-2` & `checkpoint-3`) | Nắm vững quy trình quản lý phiên bản prompt, xây dựng metrics dashboard & thiết lập ngưỡng alert SLO. |
| Lý Minh Hải (2A202601503) | QA (CP3 & Report): Điều tra incident challenge `day13-k3-observability-v1`, khoanh vùng root cause từ correlation ID & trace waterfall, đề xuất giải pháp fix (timeout/fallback) & phòng ngừa, QA validation toàn bộ hệ thống (`validate_logs.py`, `validate_dashboard.py`, `pytest`), hoàn thiện `REPORT.md`. | `CP3: document official challenge investigation and report completion` | Kỹ năng troubleshooting Observability (Metrics -> Traces -> Logs -> Root Cause), quản lý chất lượng QA và hoàn thiện báo cáo kỹ thuật. |
