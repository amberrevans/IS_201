#four digit sum of an integer

def sum ():
    number = int(input('Enter a four digit integer: '))

    thousands = number//1000
    thRemainder = number%1000

    hundreds = thRemainder//100
    hRemainder = thRemainder%100

    tens = hRemainder//10
    tRemainder = hRemainder%10

    ones = hRemainder//10
    oRemainder = hRemainder%10

    print (thousands, hundreds,tens, oRemainder)
    sum = thousands+hundreds+tens+oRemainder
    print ('The sum of the integers is:',sum)
    return
sum()
