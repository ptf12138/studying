# 服务器安全防护系统

这是一个基于 Python 的服务器安全防护系统，提供实时监控、入侵检测和安全审计功能。

## 功能特点

- 实时系统资源监控（CPU、内存、磁盘使用率）
- 端口扫描和漏洞检测
- 可疑进程检测
- 安全日志记录
- 基于 JWT 的身份验证
- 可配置的告警系统

## 系统要求

- Python 3.8+
- Linux/Windows 服务器
- 必要的系统权限

## 安装步骤

1. 克隆代码库：
```bash
git clone [repository-url]
cd security-system
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置环境变量：
```bash
export SECURITY_SYSTEM_SECRET_KEY="your-secret-key"
export ALERT_EMAIL="your-email@example.com"
export ALERT_SMTP_SERVER="smtp.example.com"
export ALERT_SMTP_PORT="587"
export ALERT_SMTP_USERNAME="your-username"
export ALERT_SMTP_PASSWORD="your-password"
```

4. 启动系统：
```bash
python main.py
```

## API 接口

系统提供以下 RESTful API 接口：

- `GET /` - 系统状态
- `GET /scan/{target}` - 端口扫描
- `GET /monitor` - 系统资源监控
- `GET /processes` - 可疑进程检测

## 安全建议

1. 定期更新系统依赖
2. 修改默认的 SECRET_KEY
3. 配置适当的防火墙规则
4. 定期检查日志文件
5. 设置强密码策略

## 注意事项

- 需要 root/管理员权限才能执行某些操作
- 建议在生产环境中使用 HTTPS
- 定期备份重要数据

## 许可证

MIT License 