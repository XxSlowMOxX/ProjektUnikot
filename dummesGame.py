import os, msvcrt, slc, random
import threading, socket

room = [str("*" * 10),str("|" + (" "*8) + "|"),str("|" + (" "*8) + "|"),str("|" + (" "*8) + "|"),str("|" + (" "*8) + "|"),str("|" + (" "*8) + "|"),str("*" * 10)]
players = []
last_message = "tets"

def insertPlayer(player, x, y):
    newRoom = room[:]
    newRow = newRoom[x][:y] + slc.bfg(player, "red", "bla")+ newRoom[x][y+1:]
    newRoom[x] = newRow
    return newRoom

def readLevel(name):
    loc = os.path.join(os.path.dirname(__file__), "levels/" + name +".map")
    with open(loc, "r+") as mapfile:
        level = mapfile.read().split("\n")
        mapfile.close()
    return level

def printLevels():
    arr = os.listdir(os.path.join(os.path.dirname(__file__), "levels/"))
    for potMap in arr:
        if(len(potMap) > 5 and potMap[-4:] == ".map"):
            print(potMap)

def levelSelector():
    os.system("cls")
    print("Available Levels are : ")
    printLevels()
    return readLevel(input("Give Level Name without trailing .map: "))[:]

def hostServer(name):
    last_message = "Server was started"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("192.168.178.54", 4230))
    while True:
        data, addr = sock.recvfrom(1024)
        print("received message: %s" % data)
    
class Player:
    rep = "v"
    def __init__(self, sx, sy, sid):
        self.x = sx
        self.y = sy
        self._id = sid
        
    def move(self,vx,vy, level):
        if(level[self.x+vx][self.y+vy] == " "):
            self.x += vx
            self.y += vy

room = levelSelector()
if(input("HOST SERVER (Y/N) ?: ") == "Y"):
    th = threading.Thread(target=hostServer, args=(1,), daemon=True)
    th.start()
myPlayer = Player(1,1,random.randint(0, 10000))
players.append(myPlayer)
i=0
while(True):
    print("Players connected: " + str(len(players)) + " | Last Message: " + last_message)
    level = insertPlayer(myPlayer.rep, myPlayer.x,myPlayer.y)
    print("\n".join(level))
    if msvcrt.kbhit():
        char = msvcrt.getch()
        if(char == b'd'):
            myPlayer.move(0,1,room)
            myPlayer.rep = ">"
        if(char == b's'):
            myPlayer.move(1,0,room)
            myPlayer.rep = "v"
        if(char == b'a'):
            myPlayer.move(0,-1,room)
            myPlayer.rep = "<"
        if(char == b'w'):
            myPlayer.move(-1,0,room)
            myPlayer.rep = "ʌ"
    i+=1
    print(i)        
    os.system("cls")


    
