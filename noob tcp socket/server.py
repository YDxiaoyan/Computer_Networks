# TCP服务端程序，支持多客户端

from socket import *
from threading import Thread

# 变量大写作为配置项
# 主机地址为空字符串，表示绑定本机所有网络接口ip地址
IP = ''
# 端口号
PORT = 50000
# 定义一次从socket缓冲区最多读入512个字节数据
BUFLEN = 512

# prompt will be shown on Server UI
# notice will be shown on Client UI


def clientHandler(dataSocket, addr):
    while True:
        recved = dataSocket.recv(BUFLEN)
        if not recved:
            prompt = f'Client {addr} has closed connection.'
            print(prompt)
            break
        # 读取的字节数据是bytes类型，需要解码为字符串
        msg = recved.decode()
        prompt = f'Message from client {addr} : {msg}'
        print(prompt)
        # 发送的数据类型必须是bytes，所以要编码
        notice = f'Message "{msg}" has been received by server.'.encode()
        dataSocket.send(notice)
    dataSocket.close()


# 实例化一个socket对象
# 参数 AF_INET 表示该socket网络层使用IP协议
# 参数 SOCK_STREAM 表示该socket传输层使用TCP协议
listenSocket = socket(AF_INET, SOCK_STREAM)

# socket绑定地址和端口
listenSocket.bind((IP, PORT))


# 使socket处于监听状态，等待客户端的连接请求 参数8 表示最多接受多少个等待连接的客户端
listenSocket.listen(8)
print(
    f'Server started successfully, waiting for clients to connect at port {PORT}')

while True:
    # listenSocket.accept() 返回的是一个元组，包含创建的用来传输数据的新的socket和客户端的地址（IP和端口号）
    dataSocket, addr = listenSocket.accept()
    prompt = f'Client {addr} has connected to server.'
    print(prompt)
    # 创建新线程处理这个客户端的消息收发
    th = Thread(target=clientHandler, args=(dataSocket, addr))
    th.start()

listenSocket.close()
