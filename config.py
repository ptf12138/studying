import os
from pathlib import Path

# 基础配置
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"

# 创建必要的目录
for directory in [LOG_DIR, DATA_DIR]:
    directory.mkdir(exist_ok=True)

# 安全配置
SECRET_KEY = os.getenv("SECURITY_SYSTEM_SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 系统监控配置
SYSTEM_MONITOR_INTERVAL = 60  # 秒
CPU_THRESHOLD = 90  # CPU使用率阈值
MEMORY_THRESHOLD = 90  # 内存使用率阈值
DISK_THRESHOLD = 90  # 磁盘使用率阈值

# 端口扫描配置
PORT_SCAN_TIMEOUT = 5  # 秒
DEFAULT_PORTS = "21,22,23,25,53,80,110,143,443,445,3306,3389,5432,5900,8080"

# 日志配置
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = LOG_DIR / "security_system.log"

# 数据库配置
DATABASE_URL = f"sqlite:///{DATA_DIR}/security_system.db"

# 告警配置
ALERT_EMAIL = os.getenv("ALERT_EMAIL", "your-email@example.com")
ALERT_SMTP_SERVER = os.getenv("ALERT_SMTP_SERVER", "smtp.example.com")
ALERT_SMTP_PORT = int(os.getenv("ALERT_SMTP_PORT", "587"))
ALERT_SMTP_USERNAME = os.getenv("ALERT_SMTP_USERNAME", "your-username")
ALERT_SMTP_PASSWORD = os.getenv("ALERT_SMTP_PASSWORD", "your-password") 