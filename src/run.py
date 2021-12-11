from welcomemenu import *
from gameplay import *
from charmenu import *



def main():
    welSeq() #Welcome Sequence
    
    player1 = playercreation()
    charmenuSeq(player1)
    chochar = player1.pchars[0]

    
    
    




 

    choice = gamestart() #see welcome menu !!!!!!!!!!!!!!!!
    game = Gameplay(choice,player1,chochar) #start game
    game.startGame(game, choice, player1, chochar)

    #move this either into gameplay or welcome menu it can't stay here


    while game.playAgain(game,player1, chochar) == "Y": #move this function into gameplay.py, playagain choice(). Then you can also use it for death
        #print("TEST stamina is %d" % chochar.stamina)
        if chochar.stamina == 0:
            print("You need to rest")
            print("You got lucky")
            print("Heres some more")
            chochar.setStamina(chochar,chochar.staminaMax)
            print("You now have %d" %chochar.stamina)
            game.startGame(game, choice, player1, chochar)
        #if 0 print you need to rest 
            # for now jsut reset stamin !REMEBER to remove this
            
        else:   #else
            game.startGame(game, choice, player1, chochar)
    
    print("Thanks for playing")

    #game finishes
    #take user input
    #start a new round


if __name__ == "__main__":
    main()