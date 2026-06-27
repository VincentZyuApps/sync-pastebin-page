# 📦 网络配置模块 —— 负责探测本机 IP、公网 IP 和端口
# 这些信息在启动时一次性确定，后面不会再变

import socket  # 🔌 用来创建一个"假连接"以获取本机局域网 IP
import urllib.request  # 🌐 用来请求 ipify.org 获取公网 IP
from pathlib import Path  # 📁 跨平台路径操作，比 os.path 好用


# 📍 当前文件所在的目录（pastebin/ 根目录）
HERE = Path(__file__).parent

# 🔌 服务监听端口，全局统一，想改端口只改这一个地方
PORT = 60628


def get_local_ip() -> str:
    """🏠 获取本机局域网 IP（比如 192.168.x.x）

    原理：建一个 UDP socket 连一个"不可能到达"的地址，
    内核会自动挑一个最合适的网卡 IP 绑定上去，
    然后用 getsockname() 把这个 IP 取回来。
    实际没有发任何数据包出去。
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))  # 🎯 随便选个地址触发路由选择
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"  # ⚠️ 如果探测失败就退回到本地回环地址
    finally:
        s.close()  # 🔒 记得关 socket
    return ip


def get_public_ip() -> str:
    """☁️ 从 ipify.org 获取公网 IP

    这个服务免费、轻量、不需要注册，返回纯文本 IP。
    如果超时或网络不通，返回"获取失败"。
    """
    try:
        req = urllib.request.Request(
            "https://api.ipify.org", headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.read().decode().strip()
    except Exception:
        return "获取失败"  # ⚠️ 没有公网 / 翻墙 / 域名解析不了 都会走到这里
