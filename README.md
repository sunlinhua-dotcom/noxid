# Private Report

Password-protected static report. AES-256-GCM encrypted content.

## Deployment

### Zeabur (default: port 8080)
- Auto-detects Python via `zbpack.json`
- Runs `python3 server.py` which binds to `$PORT` env var

### GitHub Pages
- Auto-serves `index.html` from root

### Local
```bash
python3 server.py
# Opens on http://localhost:8080
```
