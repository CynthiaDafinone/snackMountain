
import time

def pickupRCS(player):

    done ="Time's Up     "
    t = 60 #CONSTANT this is the what the timer needs to be.
    c = 0
    rcstotal = 0
    tokenCount =""
    found =""
    while t:
        mins, secs = divmod(t, 60)
         #the main counter
        rcs = tokenTimer(c) #multiplier comes after this

        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        found = " Found %d" % rcs
        print(timeformat+found , end='\r') #The Output for current state Tokens and Stamina!

        time.sleep(1)#essentially the main coundown
        t -= 1 #essentially the main coundown
        c += 1
        rcstotal = rcstotal +rcs
    print ("Time's Up")
    print ("You've won %d tokens" %rcstotal)
    #Added to inventory
    return (rcstotal)
  
#def playAgain():


    #return(done)

#create a function to set players token
#Create a dud print line to show real game output data

def addRCStoInventory(player,rcstotal):
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