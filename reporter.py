#!/usr/bin/env python3
import json, sys, datetime
from pathlib import Path
if __name__=='__main__':
    events=json.loads(Path(sys.argv[1]).read_text()) if len(sys.argv)>1 else []
    sev='low'
    if any(e.get('status')=='down' for e in events): sev='high'
    report={'generated_at': datetime.datetime.utcnow().isoformat()+'Z', 'severity': sev, 'event_count': len(events), 'events': events}
    print(json.dumps(report, indent=2))
