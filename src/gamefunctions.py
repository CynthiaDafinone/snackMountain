
import time

def pickupRCS(player, chochar):
    mod = chochar.droprate
    done ="Time's Up     "
    t = 60 #CONSTANT this is the what the timer needs to be.
    c = 0
    rcstotal = 0
    tokenCount =""
    found =""
    stamina = chochar.stamina
    


    while t:
        mins, secs = divmod(t, 60)
         #the main counter
        rcs = tokenTimer(c) #if token is collected or not
        rcs = rcs *mod #multiply by the drop rate

        timeformat = '{:02d}:{:02d}'.format(mins, secs) # Text Out Puts 
        found = " Found: %d" % rcs # Text outputs
        staminaleft = " Stamina: %d" % stamina
        blankspace = "    "
        #print(chochar.stamina)
        #print("\n")
        #Change found to single line print out print(found) - Dont do this

        print(timeformat+found+staminaleft+blankspace , end='\r') #The Output for current state Tokens and Stamina!

        time.sleep(1)#essentially the main coundown
        t -= 1 #essentially the main coundown
        c += 1
        stamina -= 1
        if stamina == 0:

            print ("\n")
            chochar.setStamina(chochar,stamina)
            rcstotal = 0 #set tokens to 0
            print("Your charachter is exhausted you dropped your tokes")
            break


        chochar.setStamina(chochar,stamina)
        rcstotal = rcstotal +rcs

    #set charachters stamina to new stamina
    print ("\n")
    print ("Time's Up")
    print ("You've won %d tokens" %rcstotal)
    #Added to inventory
    #need to create a bolean function for died, then check if died in game play and either out put you died 
    return (rcstotal)
  






#maybe create stamina timer to make it reduce every 2 second

def addRCStoInventory(player,rcstotal): #Set players tokens at end game
    currentTokens = player.tokens + rcstotal
    player.setTokens(player,currentTokens)
    return(currentTokens)



def tokenTimer(c):
    rcs = 0
    #random number generator
    #d
    if (c / 10 ).is_integer() and c>0:
        rcs = 1

        
        
    else: 
        rcs =0
        
    return(rcs) 


def staminaTimer():
    pass


def charachterMultiplier(rcs):
    pass