import socket, threading, netHelper, socketserver

messages = []
address = ("",4230)

def hostServer(name):
	srvr = socketserver.UDPServer((netHelper.getIP(), 4230), UDPHandler)
	srvr.serve_forever()

def sendMessage(name, msg):
	print(address)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(msg.encode(),address)
	print(str(sock.recv(1024), "utf-8"))

class UDPHandler(socketserver.BaseRequestHandler):
	def handle(self):
		data = self.request.recv(1024).strip()
		sock = self.request[1]
		print(self.client_address[0] + " : " + data)
		sock.sendto(data.upper(), self.client_address)

print("Chat Client Starting")
RCV_IP = input("Enter IP to connect to: ")
address = (RCV_IP, 4230)
listener = threading.Thread(target=hostServer, args=(1,),daemon=True)
listener.start()
while True:
	MSG = input("MESSAGE: ")
	sender = threading.Thread(target=sendMessage,args=(2,MSG),daemon=True)
	sender.start()