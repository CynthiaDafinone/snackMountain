
import time

def pickupRCS(player):
    done ="Time's Up"
    t = 60 #CONSTANT this is the what the timer needs to be.
    cnt = 0
    rCS = 0
    while t:
        mins, secs = divmod(t, 60)

        timeCounter = " Token"

        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat+timeCounter, end='\r') #this just looks pretty / it's irrelevant really
        time.sleep(1)#essentially the main coundown
        t -= 1 #essentially the main coundown
    return(done)



# def addRCStoInventory