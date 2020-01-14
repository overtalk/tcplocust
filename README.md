### 适用于TCP长连接的Locust压测脚本示例

* tcplocust.py Locust压测脚本示例。
* tcpserver.py Python多线程实现的TCP Ping-pong Server示例。

### 使用
- 启动
```bash
pip3 install locust
locust -f ./tcplocust.py
```

- 访问 web ui `http://localhost:8089`