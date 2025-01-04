import ipaddress

def validate_ip(ip):
    try:
        # Parse the IP address
        # if not valid then cant parse and will go to the exception
        ip_obj = ipaddress.IPv4Address(ip)
        # print(ip_obj)
        
        if ip_obj.is_private:
            print("Invalid IP")
        else:
            # valid ipv4 and not private
            print("Valid IP")
    except ipaddress.AddressValueError:
        # For invalid ip for exampel 255.255.255.256
        print("Invalid IP")

# Example Test cases
validate_ip("192.168.1.1")  # Invalid IP (Private)
validate_ip("192.169.1.1")  # Valid IP (Public)
validate_ip("172.16.0.1")   # Invalid IP (Private)
validate_ip("172.15.0.1")   # Valid IP (Public)
validate_ip("10.0.0.1")     # Invalid IP (Private)
validate_ip("8.8.8.8")      # Valid IP (Public)
validate_ip("256.256.256.256")  # Invalid IP (Invalid IPv4)
