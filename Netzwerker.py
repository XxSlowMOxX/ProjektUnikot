import socket, threading, netHelper, socketserver, time

messages = []
HOST_IP = ""
MSG_T = 0.2
PING_MSG = "PING"
last_ping = 0

opos = ""
mpos = ""

def hostServer(name):
    srvr = socketserver.UDPServer((netHelper.getIP(), 30814), UDPHandler)
    srvr.serve_forever()

def hooker(name, IP, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    global messages
    while True:
        if(len(messages) != 0):
            sock.sendto(mpos.encode(), (IP, 30814))
        opos = sock.recv(1024)
	
        time.sleep(MSG_T)

class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):

        data = self.request[0]
        sock = self.request[1]
        global last_ping
        if(str(data, "utf-8").lower() == PING_MSG.lower()):
            #print("RCVD")
            if(len(messages) != 0):
                sock.sendto(messages.pop(0).encode(), self.client_address)
            else:
                sock.sendto(str("Ping-ack").encode(), self.client_address)
        else:
            if(len(messages) != 0):
                sock.sendto(messages.pop(0).encode(), self.client_address)
            else:
                sock.sendto(str("ack").encode(), self.client_address)
            print("Received: " + str(data, "utf-8") + " and responded")

def main(mode: bool, IP="", PORT=30814):
	""" mode: True = Client; False = Host"""

	isClient = False
	if not isClient:
	    print("Server Mode Selected. Starting now...")
	    listener = threading.Thread(target=hostServer, args=(1,), daemon=True)
	    listener.start()

	else:
	    HOST_IP = input("Enter Host IP: ")
	    hook = threading.Thread(target=hooker, args=(2, IP, PORT), daemon=True)
	    hook.start()

	while True:
	    messages.append(input("MSG: "))
