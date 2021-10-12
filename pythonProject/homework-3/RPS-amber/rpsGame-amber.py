#rock paper scisors

def gt_input():

    plyr_choice = input('Enter a choice for you turn, R|P|S: ')
    if (plyr_choice.isalpha())==True:
        if ((plyr_choice.lower()=='r') or (plyr_choice.lower()=='p') \
            or (plyr_choice.lower()=='s') or (plyr_choice.lower()=='x')):
        return plyr_choice
        else:
            print ('Wrong alphabet!')
            return plyr_choice
    else:
        print ('invalid input')
        print ('follow directions')
        return gt_input()

def fn_game(a,b):

    if (a==b):
        print ('it is a tie')
    elif (a=='r') or (a)