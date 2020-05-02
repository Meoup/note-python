import socket


# 创建套接字
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip和port
server.bind(('127.0.0.1', 8000))
# 监听等待
server.listen(5)
# 获取tcp连接和连接地址
while True:
    x = 0
    conn, address = server.accept()
    print(f'接收到{address}的链接请求')
    while True:
        data = input('输入信息：')
        if data == 'q':
            conn.close()
            server.close()
            x += 1
            break
        # 给客户端发送消息
        conn.sendall(data.encode())
        # 接收客户端消息
        recv = conn.recv(1024)
        print(f'收到信息：{recv.decode()}')
    if x == 2:
        break



