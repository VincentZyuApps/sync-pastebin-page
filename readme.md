[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VincentZyu233/sync-pastebin-page)
[![Gitee](https://img.shields.io/badge/Gitee-C71D23?style=for-the-badge&logo=gitee&logoColor=white)](https://gitee.com/vincent-zyu/sync-pastebin-page)

# sync-pastebin-page

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![astral / uv](https://img.shields.io/badge/uv-FFD43B?style=for-the-badge&logo=python&logoColor=white&label=astral&labelColor=555555)](https://docs.astral.sh/uv/)

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![WebSocket](https://img.shields.io/badge/WebSocket-4A4A55?style=for-the-badge&logo=socketdotio&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

Real-time clipboard sync over LAN — type on one device, it appears on all others instantly.

## Run

```bash
uv venv --python 3.13
uv pip install fastapi uvicorn websockets
uv run uvicorn app:app --host 0.0.0.0 --port 60628
```

## Dependencies

| Package | Version | Description |
|:--------|:--------|:------------|
| [![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/) | 3.13 | Runtime |
| [![FastAPI](https://img.shields.io/badge/FastAPI-latest-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) | latest | Web framework |
| [![Uvicorn](https://img.shields.io/badge/Uvicorn-latest-000000?style=flat-square&logo=uvicorn&logoColor=white)](https://www.uvicorn.org/) | latest | ASGI server |
| [![websockets](https://img.shields.io/badge/websockets-latest-000000?style=flat-square&logo=socketdotio&logoColor=white)](https://github.com/encode/uvicorn) | latest | WebSocket protocol support |
