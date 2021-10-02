import curses

import gameclassmo
from Command import Command
import AddPlayerCommand

class JoinCommand(Command):

    name = "JOIN"

    username = ""

    def create(self, username : str):
        self.username = username

    def serialize(self) -> str:
        return ("JOIN<" + self.username + ">#")

    def deserialize(self, data : str):
        self.username = data

    def handle(self) -> dict[str, list[Command]]:
        ret : dict[str, list[Command]] = {}
        AddNew = AddPlayerCommand.AddPlayerCommand(self.Game)
        AddNew.create(self.username, 1, 1)
        ret["other"] = [AddNew]
        ret["origin"] = []
        for Player in self.Game.getPlayers():
            AddPlayer = AddPlayerCommand.AddPlayerCommand(self.Game)
            AddPlayer.create(Player.getName(), Player.getX(), Player.getY())
            ret["origin"].append(AddPlayer)

        self.Game.addPlayer(self.username, gameclassmo.Player(1,1,self.username, curses.COLOR_RED))

print(JoinCommand("SlowMO").serialize())
