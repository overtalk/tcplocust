#!/usr/bin/env python
"""使用多线程方式实现的Ping-pong Server示例。

由于线程数有上限，无法支持高并发。
"""

import socketserver


class Handler(socketserver.BaseRequestHandler):
    def read_bytes(self, length):
        """从socket读取指定数量的字节。"""
        data = bytes()
        while len(data) < length:
            chunk = self.request.recv(length - len(data))
            if chunk:
                data += chunk
            else:
                raise Exception("Error reading bytes.")
        return data

    def handle(self):
        """接收一个ping，发送一个pong。"""
        print("Handling a connection.")
        while True:
            try:
                header = self.read_bytes(4)
                length = int.from_bytes(header, 'little')
                data = self.read_bytes(length)
                if data.decode("utf-8") == "Ping":
                    res = "Pong"
                    self.request.sendall(len(res).to_bytes(4, 'little'))
                    self.request.sendall(res.encode("utf-8"))
                else:
                    raise Exception("Unrecognized protocol.")
            except Exception as e:
                print(e)
                break


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """多线程实现的TCPServer"""
    pass


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 50000
    with ThreadedTCPServer((HOST, PORT), Handler) as server:
        server.serve_forever()
