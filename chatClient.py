import os, socket, threading, netHelper

messages = []

def hostServer(name):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(netHelper.getIP(), 4230)
	print("Listener started.")
	global messages
	while(True):
		data, addr = sock.recvfrom(1024)
		print(addr.decode() + ": " + data.decode())
		messages.append(data.decode())

print()