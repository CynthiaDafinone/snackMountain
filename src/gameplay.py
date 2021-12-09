 
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
		wonTokens = pickupRCS(player) #Play actual game 
		currentTokens = addRCStoInventory(player, wonTokens)
		print("You now have %d Tokens" % currentTokens)
		#FUNCTIONstart timer
		#FUNCTION3,2,1,GO! Try to time that
		#FUNCTION 5,4,3,2,1! 
		#FUNCTIONend timer

	@staticmethod	
	def playAgain(self,player):
		option = input("Play again?")
		return option


	


	@staticmethod
	def startGame(self, choice,player):

	#choice = startChoice()
	#print(choice)
		
		if choice == "Y":
			self.playGame(player)  #while loop after this function to give option to play a second game #Take Input while input is value then play again
			
		else:
			
			#return to welcome menu
			#return to charachter menu 
			#exit game
			print("Thanks for stopping by")
	
