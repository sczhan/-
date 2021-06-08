import socket
import threading


def handle_client(conn_socket):
    # 5.接收数据
    recv_data = conn_socket.recv(1024)
    print("接收到的数据:", recv_data.decode())

    # 6.发送数据
    conn_socket.send("客户端你的数据结束到了".encode(encoding="utf-8"))

    # 7.关闭套接字
    conn_socket.close()


if __name__ == '__main__':
    # 1.创建服务端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 2. 绑定IP地址和端口号
    # tcp_server_socket.bind(("172.16.62.136", 8888))
    # 如果bind中的参数第一个ip地址元素设置为"",默认为本机ip地址
    tcp_server_socket.bind(("", 8888))

    # 3.设置监听 128:代表服务端等待排队连接的最大数量
    tcp_server_socket.listen(128)
    while True:
        # 4.等待接受客户端的连接请求 accept阻塞等待 返回一个用以和客户端通socket,客户端的地址
        conn_socket, ip_port = tcp_server_socket.accept()
        print("客户端IP地址:", ip_port)

        sub_client = threading.Thread(target=handle_client, args=(conn_socket, ))
        sub_client.start()


    # tcp_server_socket.close()
8% 306/3509 16.40   31.24mb
