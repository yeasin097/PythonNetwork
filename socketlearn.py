import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 12345

s.bind(("", PORT))

s.listen(5)

while True:
    c, address = s.accept()
    print("Got connection from ", address)

    c.send(b"thanks for connect")
