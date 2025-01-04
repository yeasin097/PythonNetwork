import nmap

def scan_devices(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sn')  # Ping scan
    devices = []
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            devices.append({
                'ip': nm[host]['addresses']['ipv4'],
                'mac': nm[host]['addresses']['mac']
            })
    return devices

# Replace '192.168.0.1/24' with your network's IP range
devices = scan_devices('192.168.0.1/24')
for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}")
