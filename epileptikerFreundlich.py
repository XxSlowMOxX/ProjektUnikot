import os, random, kbhit, curses
import threading, socket

room = []
players = []
last_message = ""

def readLevel(name):
    loc = os.path.join(os.path.dirname(__file__), "levels/" + name.decode() +".map")
    with open(loc, "r+") as mapfile:
        level = mapfile.read().split("\n")
        mapfile.close()
    return level[:]

def printLevels():
    arr = os.listdir(os.path.join(os.path.dirname(__file__), "levels/"))
    mplist = []
    for potMap in arr:
        if(len(potMap) > 5 and potMap[-4:] == ".map"):
            mplist.append(potMap)
    return mplist

def hostServer(name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("192.168.178.54", 4230))
    global last_message
    while True:
        data, addr = sock.recvfrom(1024)
        last_message = str(data) + "from" + str(addr)
        print("received message: %s" % data)

class Player:
    rep = "v"
    def __init__(self, sx, sy, sid, col):
        self.x = sx
        self.y = sy
        self._id = sid
        
		
    def move(self,vx,vy, level):
        if(level[self.x+vx][self.y+vy] == " "):
            self.x += vx
            self.y += vy

myPlayer = Player(1,1,random.randint(0, 10000),curses.COLOR_RED)
players.append(myPlayer)            
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
stdscr.addstr(0,0,"These Maps are available: \n" + "\n".join(printLevels())) #new lvlselect
stdscr.refresh()
room = readLevel(stdscr.getstr(len(printLevels())+2,0, 5)) #end of lvlselect
stdscr.clear()
stdscr.nodelay(True)
while True:
    stdscr.addstr(0,0,"\n".join(room))
    stdscr.addstr(myPlayer.x,myPlayer.y,myPlayer.rep)
    kp = stdscr.getch()
    if(kp == 3):
        exit()  
    elif(kp==ord("d")):
        myPlayer.move(0,1,room)
        myPlayer.rep = ">"
    elif(kp==ord("a")):
        myPlayer.move(0,-1,room)
        myPlayer.rep = "<"
    elif(kp==ord("w")):
        myPlayer.move(-1,0,room)
        myPlayer.rep = "ʌ"
    elif(kp==ord("s")):
        myPlayer.move(1,0,room)
        myPlayer.rep = "v"
        
    stdscr.refresh()
stdscr.refresh()
stdscr.getkey()