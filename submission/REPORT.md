# Báo cáo Day 13 Observability

Trạng thái: đã hoàn thành đến Checkpoint 2. Checkpoint 3 chờ điều tra challenge chính thức và evidence runtime tương ứng.

## 1. Thông tin nhóm

- Tên nhóm:
- Repository URL:
- Commit SHA cuối:
- Thành viên và vai trò:

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

- Challenge ID:
- Triệu chứng từ metrics:
- Trace ID liên quan:
- Log line/correlation ID liên quan:
- Root cause:
- Fix action:
- Preventive measure:

## 7. Đóng góp cá nhân

Với mỗi thành viên, ghi rõ nhiệm vụ và link commit/PR tương ứng.

| Thành viên | Phần việc | Commit/PR | Điều đã học |
|---|---|---|---|
| | | | |
