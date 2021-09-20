import os, random #random shit
import curses #rendering
import socket, threading #networking
import netHelper #helper files
import Menu #Menu for Main Menu, etc.

room = []
players = []
last_message = ""


def readLevel(name):
    loc = os.path.join(os.path.dirname(__file__), "levels/" + name +".map")
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
    sock.bind((netHelper.getIP(), 4230))
    global last_message
    while True:
        data, addr = sock.recvfrom(1024)
        last_message = str(data) + "from" + str(addr)
        print("received message: %s" % data)

def getMPOS():
    return "7,4,l"






class Player:
    name = "test"
    rep = ">"
    def __init__(self, sx, sy, sid, col, name):
        self.x = sx
        self.y = sy
        self._id = sid

    def move(self,vx,vy, level):
        if(level[self.x+vx][self.y+vy] == " "):
            self.x += vx
            self.y += vy

def rungame(stdscr):
    myPlayer = Player(1,1,random.randint(0, 10000),curses.COLOR_RED)
    players.append(myPlayer)
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    """player = Menu.menu(["Singleplayer", "Multiplayer"], stdscr)
    if (player == Menu.Singleplayer): #Singleplayer
        print("Singleplayer ist not yet possible")
        exit()
    elif (player == Menu.Multiplayer): #Multiplayer
        mode = Menu.menu(["Host", "Join"], stdscr)
        if (mode == Menu.Host):
            a = 1
            #Host Code
        elif (mode == Menu.Join):
            a =1"""

    levelIndex = Menu.menu(printLevels(), stdscr)
    room = readLevel(printLevels()[levelIndex][:-4]) #end of lvlselect

    stdscr.clear()
    curses.curs_set(0)
    stdscr.addstr(0,0,"\n".join(room))
    stdscr.addstr(myPlayer.x,myPlayer.y,myPlayer.rep)
    stdscr.refresh()
    while True:
        kp = stdscr.getch()
        if(kp!=-1):
            stdscr.addstr(0,0,"\n".join(room))
            if(kp == 113 or kp == 3):
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
            stdscr.addstr(myPlayer.x,myPlayer.y,myPlayer.rep)
            stdscr.refresh()


curses.wrapper(rungame)
