import socket, threading, netHelper

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

def sendMessage(name, msg):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(msg, (RCV_IP, 4230))

print("Chat Client Starting")
RCV_IP = input("Enter IP to connect to: ")
listener = threading.Thread(target=hostServer, args=(1,),daemon=True)
listener.start()
while True:
	MSG = input("MESSAGE: ")
	sender = threading.Thread(target=sendMessage,args=(1,MSG),daemon=True)
	sender.start()