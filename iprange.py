ip1 = input("Enter IP1: ")
ip1 = ip1.split('.')
ip1 = [int(i) for i in ip1]  # Convert the input into integers
ip2 = input("Enter IP2: ")
ip2 = ip2.split('.')
ip2 = [int(i) for i in ip2]  # Convert the input into integers

ip_address_list = []

for i in range(ip1[0], ip2[0] + 1):
    for j in range(ip1[1], ip2[1] + 1):
        for k in range(ip1[2], ip2[2] + 1):
            for l in range(ip1[3], ip2[3] + 1):
                ip_address_list.append(f"{i}.{j}.{k}.{l}")  # Using f-string for string concatenation

for address in ip_address_list:
    print(address)