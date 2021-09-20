import socket, threading, netHelper, socketserver, time
from gameclass import Game
import ast # for list <-> string parsing


messages = []
HOST_IP = ""
MSG_T = 0.2
PING_MSG = "PING"
last_ping = 0

def hostServer(name):
    srvr = socketserver.UDPServer((netHelper.getIP(), 30814), UDPHandler)
    srvr.serve_forever()


def hooker(name, HOST_IP, PORT, GAME):

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	mpos = []
	if (mpos != GAME.getMPos()):
################# FEHLT ################
	    mpos = GAME.getMPos()
################# FEHLT ################
	    sock.sendto(str(mpos).encode(), (HOST_IP, PORT))

	else:
		sock.sendto(PING_MSG.encode(), (HOST_IP, PORT))
	print(mpos)
	print("sent")
	opos =sock.recv(1024)

################# FEHLT ################
	GAME.setOPos(opos)
################# FEHLT ################

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

def getHookedorListen(GAME, isClient=True, IP="", PORT=30814,):
	""" returns thread to do stuff"""
	if(not isClient):
		isHost = True
		print("Server Mode Selected. Starting now...")
		listener = threading.Thread(target=hostServer, args=(1,), daemon=True)
		listener.start()

	else:
		print("Connecting to %s:%d"% (IP, PORT))
		hook = threading.Thread(target=hooker, args=(2, IP, PORT, GAME), daemon=True)
		hook.start()
