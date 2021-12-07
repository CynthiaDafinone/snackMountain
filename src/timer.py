import time

def countDownSimple(t):
    done = "Timer Done"
    while t:
        print(t)
        time.sleep(1)
        t-=1
    return(done)




def timer(t):
    done ="Time's Up"
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    return(done)

def cntdwnStart():
    t = 3
    print("Ready!")
    while t:
        print(t)
        time.sleep(1)
        t-=1
    print("Go!")


def timerntokens(t):
    done ="Time's Up"
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    return(done)