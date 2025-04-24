from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List
import psutil
import paramiko
import logging
from datetime import datetime
import os
from pathlib import Path

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='security_system.log'
)

# 获取当前文件所在目录
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="服务器安全防护系统",
    debug=True
)

# 配置静态文件和模板
static_dir = BASE_DIR / "static"
templates_dir = BASE_DIR / "templates"

# 确保目录存在
static_dir.mkdir(exist_ok=True)
templates_dir.mkdir(exist_ok=True)

# 挂载静态文件
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
templates = Jinja2Templates(directory=str(templates_dir))

# 安全令牌配置
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)

class SecuritySystem:
    def __init__(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
    def scan_ports(self, target: str) -> dict:
        """端口扫描"""
        # 临时返回模拟数据
        return {
            "tcp": {
                "80": {"state": "open", "name": "http"},
                "443": {"state": "open", "name": "https"},
                "22": {"state": "open", "name": "ssh"}
            }
        }
    
    def monitor_system_resources(self) -> dict:
        """系统资源监控"""
        try:
            return {
                "cpu_percent": psutil.cpu_percent(),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_usage": psutil.disk_usage('/').percent
            }
        except Exception as e:
            logging.error(f"系统资源监控错误: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))
    
    def check_suspicious_processes(self) -> List[dict]:
        """检查可疑进程"""
        suspicious_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'status']):
            try:
                process_info = proc.info
                suspicious_processes.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return suspicious_processes

security_system = SecuritySystem()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    logging.info("访问首页")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/scan/{target}")
async def scan_ports(target: str, token: str = Depends(oauth2_scheme)):
    logging.info(f"扫描端口: {target}")
    return security_system.scan_ports(target)

@app.get("/monitor")
async def monitor_resources(token: str = Depends(oauth2_scheme)):
    logging.info("获取系统资源数据")
    return security_system.monitor_system_resources()

@app.get("/processes")
async def check_processes(token: str = Depends(oauth2_scheme)):
    logging.info("获取进程列表")
    return security_system.check_suspicious_processes()

if __name__ == "__main__":
    import uvicorn
    logging.info("启动服务器")
    uvicorn.run(
        "main:app",  # 修改为导入字符串
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug"
    )