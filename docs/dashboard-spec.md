# Dashboard specification

`config/dashboard.yaml` is the machine-validated contract. The dashboard reads `data/logs.jsonl`; `GET /metrics` exposes the same six groups as runtime snapshots. Use a 60-minute default range, refresh every 30 seconds, and show each threshold as an SLO line.

| Group | Dashboard data | Runtime metric(s) | Unit | Visualization | Threshold |
| --- | --- | --- | --- | --- | --- |
| Latency | `response_sent.latency_ms` P50/P95/P99 | `latency_p50`, `latency_p95`, `latency_p99` | ms | percentile time series | P95 <= 3000 ms |
| Traffic | `request_received` count/rate | `traffic` | requests/minute | count time series | >= 1 request/minute |
| Error | `request_failed` rate and `error_type` breakdown | `error_rate_pct`, `error_breakdown` | percent | rate plus breakdown | <= 2% |
| Cost | `response_sent.cost_usd` total and average | `total_cost_usd`, `avg_cost_usd` | USD | time series plus summary | <= 2.5 USD/day |
| Tokens | `response_sent.tokens_in`, `response_sent.tokens_out` | `tokens_in_total`, `tokens_out_total` | tokens | dual-series totals | <= 50,000 tokens |
| Quality | `response_sent.quality_score` mean | `quality_avg` | score (0-1) | average time series | >= 0.75 |

The dashboard tool may be Streamlit, Grafana, a notebook, or equivalent; Langfuse is used for trace and prompt investigation rather than as the dashboard data source. Build exactly these six conceptual groups, then validate the contract before collecting UI evidence:

```bash
python scripts/validate_dashboard.py
```
