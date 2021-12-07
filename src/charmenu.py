from charachter import *
from player import *
import time

#for now pass in random values for each one to make game work

def createChars(name, stamina,droprate, price):

	char1 = Charachter(name, stamina,droprate, price)
	return(char1)


def buildcharlist():
	#DEMO THIS WILL BE AT LEAST a CSV sheet tomorrow [READ FROM CSV]
	chars = []
	char1 = createChars("Jeff", 100, 0.5, 0.5)
	char2 = createChars("Alice", 120, 0.4, 0.7)
	char3 = createChars("Jake", 90, 0.2, 0.3)
	#print(char1.name)
	chars.append(char1)
	chars.append(char2)
	chars.append(char3)
	

	return(chars)


	



#-----------------------------------------------------------------------------
def showCharachters(chars):
	print("Choose your charachter!!!")
	time.sleep(3)
	i = 0
	for char in chars:
		i+= 1 
		print("\n\n")
		print("--Option-- %d" % i)
		print("Name:  %s." % char.name)
		print("Stamina: %d" % char.stamina)
		print("Droprate: %.2f" % char.droprate)
		print("Price: %.2f" % char.droprate)
		
		time.sleep(1)

		#scale this down with CSV tomorrow also



def playerChoose(player,chars):
	#print(player)
	pchars = player.pchars
	option = input("Choose your charachter? Press 1 for Option 1...")
	ioption = int(option)

	pcharchoice = chars[ioption-1]

    #Break this up - move this to add to player
	
	#print(pchars[0].name)
	pchars.append(pcharchoice)
	return(player)
	

	#return(name)


	#print(player.name)
	#print(player.wallet)
	#print(chars)


def addtoPlayer(pcharchoice):
	
	return



def charmenuSeq(player1):
	chars = buildcharlist()
	showCharachters(chars)
	player1  = playerChoose(player1,chars) 

	#print(player1)
	chochars = player1.pchars
	chochar = chochars[0]
	print("\n\n")
	print("--YOU CHOSE %d--")
	print("Name:  %s." % chochar.name)
	print("Stamina: %d" % chochar.stamina)
	print("Droprate: %.2f" % chochar.droprate)
	print("Price: %.2f" % chochar.droprate)
	return(chochar)

