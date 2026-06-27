> **[📖 English](readme.md)**
> **[📖 简体中文(大陆)](readme.zh-cn.md)**

![sync-pastebin-page](https://socialify.git.ci/VincentZyuApps/sync-pastebin-page/image?description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Ficon.icepanel.io%2FTechnology%2Fsvg%2FFastAPI.svg&name=1&owner=1&stargazers=1&theme=Auto)

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VincentZyu233/sync-pastebin-page)
[![Gitee](https://img.shields.io/badge/Gitee-C71D23?style=for-the-badge&logo=gitee&logoColor=white)](https://gitee.com/vincent-zyu/sync-pastebin-page)

# 📋 sync-pastebin-page

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![astral / uv](https://img.shields.io/badge/uv-FFD43B?style=for-the-badge&logo=python&logoColor=white&label=astral&labelColor=555555)](https://docs.astral.sh/uv/)

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![WebSocket](https://img.shields.io/badge/WebSocket-4A4A55?style=for-the-badge&logo=socketdotio&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

局域网内实时剪贴板同步 — 在一个设备上输入，所有设备立即同步显示。

## 🎯 示例场景

比如局域网内的两台手机和电脑之间临时同步文字或图片。不想装微信 QQ，直接用浏览器打开链接即可。

## 🖼️ 预览

| PC | Phone |
|:-:|:-:|
| ![PC](docs/images/preview/preview.pc.png) | ![Phone](docs/images/preview/preview.phone.png) |

## 🚀 运行

```bash
uv venv --python 3.13
uv pip install fastapi uvicorn websockets
uv run uvicorn app:app --host 0.0.0.0 --port 60628
```

## 📦 依赖

| Package | Version | Description |
|:--------|:--------|:------------|
| [![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/) | 3.13 | 运行环境 |
| [![FastAPI](https://img.shields.io/badge/FastAPI-latest-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) | latest | Web 框架 |
| [![Uvicorn](https://img.shields.io/badge/Uvicorn-latest-000000?style=flat-square&logo=uvicorn&logoColor=white)](https://www.uvicorn.org/) | latest | ASGI 服务器 |
| [![websockets](https://img.shields.io/badge/websockets-latest-000000?style=flat-square&logo=socketdotio&logoColor=white)](https://github.com/encode/uvicorn) | latest | WebSocket 协议支持 |
