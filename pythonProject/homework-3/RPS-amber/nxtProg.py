import random

def roll_dice ():
    dice1 = random.randint(1,6)
    print ('First dice:',dice1)
    dice2 = random.randint(1,6)
    print ('Second dice:',dice2)
    total = dice1 + dice2
    print ('total is',total)
    if (total ==7):
        print ('Winner!')
    else:
        print ("You lost.")
roll_dice()