import time
from player import *
from gameplay import *

def startLogo():

	logo = "***SNACK MOUNTAIN***"
	welcome = "\nWelcome to snack mountain..."
	return logo+welcome 
	#time delay practice
	

def enterName():
	name = input("What is your name? ")
	print("Hello, %s." % name)
	return(name)



def enterWallet():
	wallet = input("What is your wallet address? ")
	return(wallet)


def createPlayer():
	name = enterName()
	wallet = enterWallet()
	

	player1 = Player(name,wallet)
	print("Thanks, %s." % name)
	
	return(player1)


def instructions():
	time.sleep(2)
	return("You need wallet to play")
	



def startChoice():
	choice = input("Start Game? Y/N ")
	#print(choice)
	if choice == "Y" or choice =="N":
		dec  = choice
	else: 
		print("try again")
		choice = input("Start Game? Y/N ")
		dec = choice

	return dec 
	
def moreSoon():

	time.sleep(3)
	soon = "...more coming soon"


	return soon

	
	
#RUN OUTSIDE OF file	

def welSeq(): #sequence of tasks.[Separate into, pre-game, welcome and menu]

	#Welcome sequence!!
	#Create characters here
	print(startLogo())
	print(instructions())
	
	
	
	
	
	
	


def playercreation():
	player1 = createPlayer() #MOVE THIS into it's own file potentially maybe
	#print(moreSoon())
	return player1


#---------------Option for selecting pre-existing player


def gamestart():
	choice = startChoice()
	return(choice)






