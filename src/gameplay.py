
from timer import *
from gamefunctions import *

class Gameplay:

	def __init__(this, choice, player):
		this.choice = choice
		this.player = player

	
	def playGame(self, player):
		print("starting now")
		cntdwnStart()#NOT IMPORTANT but fun
		#print(timer(30))
		print(pickupRCS(player))
		#FUNCTIONstart timer
		#FUNCTION3,2,1,GO! Try to time that
		#FUNCTION 5,4,3,2,1! 
		#FUNCTIONend timer

	@staticmethod
	def startGame(self, choice,player):

	#choice = startChoice()
	#print(choice)
		
		if choice == "Y":
			self.playGame(player)
		else:
			print("Thanks for stopping by")
	
