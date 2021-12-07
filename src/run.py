from welcomemenu import *
from gameplay import *
from charmenu import *



def main():
    welSeq() #Welcome Sequence
    
    player1 = playercreation()
    charmenuSeq(player1)
    #chosen charachter = player1.pchars[0]

    
    
    




 

    choice = gamestart()
    game = Gameplay(choice,player1) #start game
    game.startGame(game, choice, player1)


if __name__ == "__main__":
    main()