import socket
import time


if __name__ == '__main__':
    # 1.创建客户端套接字对象
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.和服务端套接字建立连接
    tcp_client_socket.connect(("127.0.0.1", 8888))

    # 3.发送数据
    time.sleep(15)
    tcp_client_socket.send("1".encode(encoding="utf-8"))

    # 4.接收数据 recv阻塞等待数据的到来
    recv_data = tcp_client_socket.recv(1024)
    print(recv_data.decode(encoding='utf-8'))

    # 5.关闭客户端套接字
    tcp_client_socket.close()