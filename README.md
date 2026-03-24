# automated-incident-reporter

A Python CLI that converts a list of incident events into a single normalized JSON incident report with a generated timestamp and a basic severity score.

## Key features

- Reads events from a JSON file
- Marks severity as high if any event contains status=down
- Includes UTC generation timestamp
- Outputs a ready-to-forward JSON report

## Project structure

- `reporter.py` — Builds the final incident report
- `requirements.txt` — Dependency file (empty; only standard library is used)

## Requirements

- Python 3.9+

## Setup

```bash
git clone https://github.com/biprajit007/automated-incident-reporter.git
cd automated-incident-reporter
```

## Usage

### events.json

```bash
[{"service":"api","status":"down"},{"service":"db","status":"degraded"}]
```

### Generate report

```bash
python3 reporter.py events.json
```

## Sample output

```text
{
  "generated_at": "2026-03-24T00:00:00Z",
  "severity": "high",
  "event_count": 2,
  "events": [...]
}
```

## Limitations / next improvements

- Severity logic is intentionally simplistic
- No schema validation beyond whatever fields your JSON contains
- No integrations for email, Slack, or ticket systems yet
