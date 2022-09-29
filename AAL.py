from time import sleep
from os import system

class cell():
	cell_number = 0
	cell_speed = 0
	#cell_size = 0 in aother versions
	cell_huneger = 0

def game():
	pass

def setup():
	pass

def draw(world):
	system("clear")
	for x in range(len(world)):
		for y in range(len(world)):
			print(f"{x}, {y}",end="")
		print()

def main():
	FPS = 1
	world = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
	setup()
	while True:
		draw(world)
		game()
		sleep(FPS)
if __name__ == "__main__":
	main()
