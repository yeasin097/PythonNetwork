import os

result = os.system("ifconfig | grep inet")

print(result)