import os
import socket
import threading

target_host = input("Enter target host IP address or hostname: ")
start_port = 1
end_port = 65535

if os.path.exists("open_ports.txt"):
    with open("open_ports.txt", "a") as f:
        f.write("\n")


def port_scan(port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        client.connect((target_host, port))

        with open("open_ports.txt", "a") as f:
            f.write(f"{target_host}:{port}\n")

        client.close()
    except:
        print(f"\033[31m[-]\033[0m {target_host}:{port}")
        pass


for port in range(start_port, end_port + 1):
    t = threading.Thread(target=port_scan, args=(port,))
    t.start()
