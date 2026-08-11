# Alert runbooks

All alerts are symptom-based. Investigate from metrics to traces to correlated structured logs; do not use raw request data.

## Alert 1

- Name: `high_latency_p95`
- Severity: warning
- Related SLI/SLO: `latency_p95_ms`, objective below 3000 ms (99.5% target).
- Trigger: `latency_p95 > 3000ms for 5 minutes`.
- User impact: users experience slow chat responses and may time out.
- First three investigation steps:
  1. Confirm the P95 latency increase and affected time window in the Latency dashboard panel.
  2. Open a slow Langfuse trace and inspect the `run` waterfall, including `retrieve` and `generate` spans.
  3. Use the trace `correlation_id` to find the matching `request_received` and `response_sent` records in `data/logs.jsonl`.
- Temporary mitigation: disable the affected incident/source if safe, reduce expensive retrieval, and communicate degraded response times.
- Owner: on-call-engineer

## Alert 2

- Name: `elevated_error_rate`
- Severity: critical
- Related SLI/SLO: `error_rate_pct`, objective below 2% (99.0% target).
- Trigger: `error_rate_pct > 5 for 3 minutes`.
- User impact: chat requests fail and users cannot receive answers.
- First three investigation steps:
  1. Confirm the error-rate increase and error breakdown in the Error dashboard panel.
  2. Open failing Langfuse traces for the affected feature or model and identify the failed span.
  3. Use each trace `correlation_id` to inspect correlated `request_failed` logs and their `error_type` values.
- Temporary mitigation: disable the failing dependency/feature when possible, route users to a known-good path, and retry only safe transient failures.
- Owner: on-call-engineer

## Alert 3

- Name: `cost_budget_exceeded`
- Severity: warning
- Related SLI/SLO: `daily_cost_usd`, objective below 2.5 USD/day (100.0% target).
- Trigger: `daily_cost_usd > 2.5`.
- User impact: service remains available, but the daily operating budget is at risk.
- First three investigation steps:
  1. Confirm the daily total and average request cost in the Cost dashboard panel.
  2. Inspect high-cost Langfuse traces by feature and model, including token usage on the generation.
  3. Use trace `correlation_id` values to inspect correlated request and response logs for token and cost fields.
- Temporary mitigation: disable cost-spike behavior, apply a lower-cost model or response/token limit, and pause nonessential traffic.
- Owner: team-lead
