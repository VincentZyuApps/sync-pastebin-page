# 🚀 应用入口 —— 组装各个模块，启动 FastAPI 服务

# 🧩 第三方依赖
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# 📦 本地模块
from network import HERE, PORT, get_local_ip, get_public_ip
from routes import router

# 🌐 启动时探测网络信息（只跑一次）
local_ip = get_local_ip()  # 局域网的 IP
public_ip = get_public_ip()  # 公网的 IP（可能获取失败）

# 🖨️ 启动信息展示
print()
print(f"  🟢 PasteBin Server Started")
print(f"  🌐 局域网  http://{local_ip}:{PORT}")
print(f"  ☁️  公网    http://{public_ip}:{PORT}")
print(f"  💻 本机    http://127.0.0.1:{PORT}")
print()

# 🏗️ 创建 FastAPI 实例
app = FastAPI()

# 📁 挂载静态文件目录（字体、图片等可以通过 /assets/xxx 访问）
app.mount("/assets", StaticFiles(directory=str(HERE / "assets")), name="assets")

# 🛣️ 注册路由（网页 + WebSocket 都是 routes.py 里定义的）
app.include_router(router)
