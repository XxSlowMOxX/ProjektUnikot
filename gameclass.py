class Game:
	def __init__(self, Players):
		self.Players = Players

	def addPlayer(self,player):
		self.Players.append(player)
	
	def getMPos(self):
		return [self.Players[0].x, self.Players[0].y, self.Players[0].rep]
	
	def setOPos(self, opos):
		# TODO 
		self.Players[1].x = opos[0]
		self.Players[1].y = opos[1]
		self.Players[1].rep = opos[2]
