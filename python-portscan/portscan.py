#!/usr/bin/python3
import sys,socket

if len(sys.argv) <= 1:
    print("[PORTSCAN] - MODO DE USO")
    print("./portscan.py 192.168.0.1")
else:
    ip = sys.argv[1]
    for porta in range(1,65537):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if (sock.connect_ex((ip,porta)) == 0):
            print("[PORTA ABERTA] - ",porta)
            sock.close()
