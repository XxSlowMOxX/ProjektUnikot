class Player:
    def __init__(self, sx, sy, sid, col):
        self.x = sx
        self.y = sy
        self.id = sid
        self.rep = ">"

    def move(self, vx : int, vy : int, level : str):
        if(level[self.x+vx][self.y+vy] == " "):
            self.x += vx
            self.y += vy

    def getX(self) -> int:
        return self.x

    def getY(self) -> int:
        return self.y

    def getName(self) -> str:
        return self.id


class Game:

    Players = {}

    def __init__(self, level):
        self.Level = level

    def addPlayer(self, id : str, player : Player):
        self.Players[id] = player
    
    def getPos(self, id : str):
        return [self.Players[id].x, self.Players[id].y, self.Players[id].rep]
    
    def getPlayer(self, id : str) -> Player:
        return self.Players[id]

    def getPlayers(self) -> list[Player]:
        return self.Players.values()
