import socket, threading, netHelper, socketserver, time
import random
from gameclass import Game, Player
import ast # for list <-> string parsing


messages = []
MSG_T = 0.01
PING_MSG = "PING"
last_ping = 0

def hostServer(name, IP):
    #srvr = socketserver.UDPServer((netHelper.getIP(), 30814), UDPHandler)
    srvr = socketserver.UDPServer((IP, 30814), UDPHandler)
    srvr.serve_forever()


def hooker(name, HOST_IP, PORT, GAME): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        mpos = GAME.getMPos()
        sock.sendto(str(mpos).encode(), (HOST_IP, PORT))


        opos = sock.recv(1024).decode()
        opos = ast.literal_eval(opos)

        if len(GAME.Players)==1:
            GAME.addPlayer(Player(opos[0],opos[1], random.randint(0,10000), "dummy"))

        GAME.setOPos(opos)

        time.sleep(MSG_T)


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0]
        sock = self.request[1]

        opos = ast.literal_eval(str(data, "utf-8"))
        if len(GAME.Players)==1:
            GAME.addPlayer(Player(opos[0],opos[1], random.randint(0,10000), "dummy"))

        GAME.setOPos(opos)
        sock.sendto(str(GAME.getMPos()).encode(), self.client_address)


def getHookedorListen(game, isClient=True, IP="", PORT=30814,):

    if(not isClient):
        global GAME
        GAME = game
        listener = threading.Thread(target=hostServer, args=(1,IP), daemon=True)
        listener.start()

    else:
        print("Connecting to %s:%d"% (IP, PORT))
        hook = threading.Thread(target=hooker, args=(2, IP, PORT, game), daemon=True)
        hook.start()
