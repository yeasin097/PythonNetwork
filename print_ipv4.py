import socket

host_name = socket.gethostname()

print(host_name)

ipv4_address = socket.gethostbyname(host_name)

print(ipv4_address)
