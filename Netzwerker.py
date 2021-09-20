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
        mpos = GAME.getMPos()
        sock.sendto(str(mpos).encode(), (HOST_IP, PORT))

    else:
        sock.sendto(PING_MSG.encode(), (HOST_IP, PORT))

    opos = sock.recv(1024)
    opos = ast.literal_eval(opos)
    print(opos)

    GAME.setOPos(opos)

    time.sleep(MSG_T)


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):

        data = self.request[0]
        sock = self.request[1]
        GAME.setOPos(ast.literal_eval(str(data, "utf-8"))

        sock.sendto(str(GAME.getMPos()), self.client_address)


def getHookedorListen(GAME, isClient=True, IP="", PORT=30814,):
    if(not isClient):
        isHost = True
        print("Server Mode Selected. Starting now...")
        listener = threading.Thread(target=hostServer, args=(1,GAME), daemon=True)
        listener.start()

	else:
            print("Connecting to %s:%d"% (IP, PORT))
            hook = threading.Thread(target=hooker, args=(2, IP, PORT, GAME), daemon=True)
            hook.start()
