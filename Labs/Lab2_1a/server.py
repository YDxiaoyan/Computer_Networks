from socket import *
# In order to terminate the program
import sys

# 参数 AF_INET 表示该socket网络层使用IP协议
# 参数 SOCK_STREAM 表示该socket传输层使用TCP协议
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
# 主机地址为空字符串，表示绑定本机所有网络接口ip地址
IP = ''
# 端口号
PORT = 5555

serverSocket.bind((IP, PORT))
serverSocket.listen(1)

# 定义一次从socket缓冲区最多读入512个字节数据
BUFLEN = 1024

while True:
    # Establish connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        # 读取的字节数据是bytes类型，需要解码为字符串
        message = connectionSocket.recv(BUFLEN).decode()
        print(
            f'Message is: \n-----------------------\n{message}-----------------------')
        filename = message.split()[1]
        print(
            f'Filename is: \n-----------------------\n{filename}\n-----------------------\n')
        f = open(filename[1:])
        outputdata = f.read()
        print(
            f'Outputdata is: \n-----------------------\n{outputdata}-----------------------\n')

        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        # connectionSocket.send('\r\n'.encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send('\n404 Not Found\n\n'.encode())

        # Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
