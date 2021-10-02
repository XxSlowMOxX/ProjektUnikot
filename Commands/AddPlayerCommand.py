import gameclassmo
import curses
from Command import Command

class AddPlayerCommand(Command):

    name = "ADDPLAYER"

    def __init__(self, Game : gameclassmo.Game):
        Command.__init__(Game)

    def create(self, username: str, x : int, y : int):
        self.username = username
        self.x = x
        self.y = y

    def serialize(self) -> str:
        return ("ADDPLAYER<" + self.username + ";" + str(self.x), ";" + str(self.y) + ">#")

    def deserialize(self, data : str):
        dat = data.split(";")
        self.username = dat[0]
        self.x = int(dat[1])
        self.y = int(dat[2])
        return

    def handle(self) -> None:
        self.Game.addPlayer(self.username, gameclassmo.Player(self.x, self.y, self.username, curses.COLOR_RED))
        return