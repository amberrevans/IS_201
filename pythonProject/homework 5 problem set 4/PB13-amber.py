#number of notes in given amount
#was not sure what this one meant, count the bills or give the total of bills

def noteCount (amount):
    notes = [100, 50, 20, 10, 5, 1]

    currencyCount=[ 0, 0, 0, 0, 0, 0]

    print ('Number of notes in amount: ')

    for i,j in zip(notes, currencyCount):
        if amount >=i:
            j= amount //i
            amount = amount -j*i
            print (i,':',j)

amount = int(input('Enter an amount: '))
noteCount (amount)
