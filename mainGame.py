import os
import random  # random shit
import curses  # rendering
import socket, threading, netHelper  # helper files; get you IP
import Netzwerker  # getHookedorListen function
from gameclass import Game, Player
import netHelper  # helper files
import Menu  # Menu for Main Menu, etc.
import time

room = []
players = []
last_message = ""


def readLevel(name):
    loc = os.path.join(os.path.dirname(__file__), "levels/" + name + ".map")
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




def rungame(stdscr):
    myPlayer = Player(1, 1, random.randint(0, 10000), curses.COLOR_RED)
    # own Player always FIRST Player, was btw ne blöde Idee ist
    GAME = Game([myPlayer])
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)

    mainMenu = Menu.menu(["Singleplayer", "Multiplayer"], stdscr)

    if (mainMenu == Menu.Singleplayer):
        exit()

    elif (mainMenu == Menu.Multiplayer):
        mpMode = Menu.menu(["Host", "Join"], stdscr)

        if (mpMode == Menu.Host):
            Netzwerker.getHookedorListen(
                    GAME, isClient=False, IP="192.168.2.134", PORT=30814)

        elif (mpMode == Menu.Join):
            myPlayer.x +=1
            Netzwerker.getHookedorListen(
                GAME, isClient=True, IP="192.168.2.134", PORT=30814)


    levelIndex = Menu.menu(printLevels(), stdscr)
    room = readLevel(printLevels()[levelIndex][:-4])

    stdscr.clear()
    curses.curs_set(0)
    stdscr.addstr(0, 0, "\n".join(room))
    for player in GAME.Players:
        stdscr.addstr(player.x, player.y, player.rep)

    stdscr.refresh()
    stdscr.nodelay(True)

    while True:
        kp = stdscr.getch()
        # DEBUGgging
        stdscr.addstr(13,1,str(time.time()))



        stdscr.addstr(0, 0, "\n".join(room))

        for player in range(len(GAME.Players)):
            # yes this is ugly
            stdscr.addstr(GAME.Players[player].x, GAME.Players[player].y, "-")

        if (kp == 113 or kp == 3):
            exit()
        elif (kp == ord("d")):
            myPlayer.move(0, 1, room)
            myPlayer.rep = ">"
        elif (kp == ord("a")):
            myPlayer.move(0, -1, room)
            myPlayer.rep = "<"
        elif (kp == ord("w")):
            myPlayer.move(-1, 0, room)
            myPlayer.rep = "ʌ"
        elif (kp == ord("s")):
            myPlayer.move(1, 0, room)
            myPlayer.rep = "v"

        for player in range(len(GAME.Players)):
            # yes this is ugly
            stdscr.addstr(10+player,1, str(GAME.Players[player].x)+
                    ","+str(GAME.Players[player].y)+" "+GAME.Players[player].rep)
            stdscr.addstr(GAME.Players[player].x, GAME.Players[player].y, GAME.Players[player].rep)

        stdscr.refresh()

curses.wrapper(rungame)
