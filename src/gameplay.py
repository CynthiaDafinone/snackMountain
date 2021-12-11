 
from timer import *
from gamefunctions import *

class Gameplay:

	def __init__(this, choice, player, chochar):
		this.choice = choice
		this.player = player
		this.chochar = chochar

	
	def playGame(self, player, chochar):
		print("starting now")
		cntdwnStart()#NOT IMPORTANT but fun
		#print(timer(30))




		


		wonTokens = pickupRCS(player, chochar) #Play actual game 

		#gameoutput {won/died,wonTokens,stamina value(maybe no need for stamina value pulled here)} 

		#DEATH CHECK GOES HERE
		#if won the run as normal, if not print you died and no tokens. Return in tuple with won tokens 
		#dont add tokens figure out full functionality later
		currentTokens = addRCStoInventory(player, wonTokens)
		print("You now have %d Tokens" % currentTokens)
		#FUNCTIONstart timer
		#FUNCTION3,2,1,GO! Try to time that
		#FUNCTION 5,4,3,2,1! 
		#FUNCTIONend timer

	@staticmethod	
	def playAgain(self,player, chochar):
		option = input("Play again?")
		return option


	


	@staticmethod
	def startGame(self, choice,player, chochar):
		#check to start game for now just stamin but eventually health and other thigns too
		
		
		if choice == "Y": #AND stamina for now but later
			
			if chochar.stamina == 0:
				print("You need to rest")
				print("You got lucky")
				print("Heres some more")
				chochar.setStamina(chochar,chochar.staminaMax)
				print("You now have %d" %chochar.stamina)
				self.playGame(player, chochar)

			else:

				self.playGame(player, chochar)  #while loop after this function to give option to play a second game #Take Input while input is value then play again
			
		else:
			
			#return to welcome menu
			#return to charachter menu 
			#exit game
			print("Thanks for stopping by")
	
