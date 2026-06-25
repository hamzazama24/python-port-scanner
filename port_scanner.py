import socket

target = "scanme.nmap.org"
ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]

print(f"Scanning target: {target}\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is closed")

    s.close()
