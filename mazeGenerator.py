import random

map_x = 100
map_y = 100

def generateMap():
	maze = [["─" for i in range(map_x)]]
	for i in range(map_y-2):
		maze.append(["|"+" "*(map_x-2)+"|"])


	
