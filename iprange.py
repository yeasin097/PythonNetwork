ip1=input("Enter IP1: ")
ip1 = ip1.split('.')
ip1 = [eval(i) for i in ip1]
ip2=input("Enter IP2: ")
ip2 = ip2.split('.')
ip2 = [eval(i) for i in ip2]

for i in range(ip1[0],ip2[0]):
    for j in range(ip1[1],ip2[1]):
        for k in range(ip1[2],ip2[2]):
            for l in range(ip1[3],ip2[3]):
                print(i+"."+j+"."+k+"."+l)