'''
━━━━┏━━━┓┏━━━┓┏┓━━━━━━━━━━━┏┓━━┏━━━┓━┏┓━
━━━━┃┏━┓┃┃┏━┓┃┃┃━━━━━━━━━━━┃┃━━┃┏━┓┃┏┛┗┓
┏━┓━┃┃━┃┃┃┃━┃┃┃┗━┓┏┓┏┓┏┓━┏┓┃┗━┓┃┃━┃┃┗┓┏┛
┃┏┓┓┃┃━┃┃┃┃━┃┃┃┏┓┃┗╋╋┛┃┃━┃┃┃┏┓┃┃┃━┃┃━┃┃━
┃┃┃┃┃┗━┛┃┃┗━┛┃┃┗┛┃┏╋╋┓┃┗━┛┃┃┗┛┃┃┗━┛┃━┃┗┓
┗┛┗┛┗━━━┛┗━━━┛┗━━┛┗┛┗┛┗━┓┏┛┗━━┛┗━━━┛━┗━┛
━━━━━━━━━━━━━━━━━━━━━━┏━┛┃━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━┗━━┛━━━━━━━━━━━━━━
'''

import socket, time, sys

hostinput = input("Enter Hostname/IP: ")
hostIP = socket.gethostbyname(hostinput)
print("Scanning:", hostIP)
start = time.time()

try:
    for port in range(65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status = sock.connect_ex((hostIP, port))
        if status == 0:
            print (f'port {port} is open')
        sock.close()
except socket.error:
    sys.exit()

end = time.time()
print(f'Time taken {end-start:.2f} seconds')
