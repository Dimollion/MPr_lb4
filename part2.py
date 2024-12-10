import socket


def multi_client_server():
    HOST = '127.0.0.1'
    PORT = 50007
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ser_sock:
        ser_sock.bind((HOST, PORT))
        ser_sock.listen(10)
        print('Server works at: ', HOST, ' ', PORT)

        while True:
            conn, addr = ser_sock.accept()
            print('Client connected from: ', addr, end = ' Recieved data: ')
            handle_client(conn)


def handle_client(conn):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode())
            conn.sendall(data)


if __name__ == '__main__':
    multi_client_server()