#!/usr/bin/env python3
import socket
import argparse

parser = argparse.ArgumentParser(description='Test to see if you can send IPv6 packets to another through NAT')
parser.add_argument('--address',
                    '-a',
                    default="::1",
                    help='IPv6 address of remote end')
args = parser.parse_args()

REMOTE_IP = args.address

UDP_IP = "::" # = 0.0.0.0 u IPv4
UDP_PORT = 51441

sock = socket.socket(socket.AF_INET6, # Internet
						socket.SOCK_DGRAM) # UDP
sock.settimeout(1)
sock.bind((UDP_IP, UDP_PORT))

MESSAGE = b'Hello, the connection works!!!'

def send_hello():
    sock.sendto(MESSAGE, (REMOTE_IP, UDP_PORT))

while True:
    data = None
    try:
        data, addr = sock.recvfrom(1024)
    except socket.timeout:
        print("Listening for data...")
        send_hello()
        continue

    print("received message:", data)
