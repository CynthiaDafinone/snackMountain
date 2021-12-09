from welcomemenu import *
from gameplay import *
from charmenu import *



def main():
    welSeq() #Welcome Sequence
    
    player1 = playercreation()
    charmenuSeq(player1)
    #chosen charachter = player1.pchars[0]

    
    
    




 

    choice = gamestart() #see welcome menu !!!!!!!!!!!!!!!!
    game = Gameplay(choice,player1) #start game
    game.startGame(game, choice, player1)

    #move this either into gameplay or welcome menu it can't stay here

    while game.playAgain(game,player1) == "Y":
        game.startGame(game, choice, player1)
    else:
        print("Thanks for playing")

    #game finishes
    #take user input
    #start a new round


if __name__ == "__main__":
    main()