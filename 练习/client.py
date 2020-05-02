import socket


# 创建套接字对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
client.connect(('127.0.0.1', 8000))
while True:
    # 接收信息
    data = client.recv(1024)
    print(f'收到信息：{data.decode()}')
    s = input('输入信息：')
    if s == 'q':
        client.close()
        break
    # 发送信息
    client.sendall(s.encode())

