import socket
import threading

HEADER = 3048
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
# DISCONNECT_MESSAGE = "!TC!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        file = conn.recv(HEADER).decode(FORMAT)
        if file:
            print("File recieved ....")
            print(file)
            connected = False

        # msg_length = conn.recv(HEADER).decode(FORMAT)
        #
        # if msg_length:
        #     msg_length = int(msg_length)
        #     msg = conn.recv(msg_length).decode(FORMAT)
        #
        #     if msg == DISCONNECT_MESSAGE:
        #         connected = False
        #
        #     print(f"[{addr}]: {msg}")
    # conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is rendered on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


if __name__ == "__main__":
    print("[STARTING] server is starting ")
    start()
