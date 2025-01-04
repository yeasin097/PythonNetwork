from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    # Create an ARP request packet
    arp_request = ARP(pdst=ip_range)
    # Create an Ethernet frame
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine them
    arp_request_broadcast = broadcast / arp_request
    # Send the packet and capture the response
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    devices = []
    for sent, received in answered_list:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

# Replace '192.168.0.1/24' with your network's IP range
network_devices = scan_network("192.168.0.1/24")
for device in network_devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}")
