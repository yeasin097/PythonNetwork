import socket

remote_host = "www.cuet.ac.bd"

ip = socket.gethostbyname(remote_host)

print(ip)