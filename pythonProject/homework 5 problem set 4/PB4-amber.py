#number is divisable by 5 and 11 or not
#not sure if that is what was meant vs or a number divisable by 5 or 11


num = int(input('Enter any positive number: '))

if((num %5 ==0) and (num % 11==0)):
    print (num, 'is divisible by 5 and 11.')
else:
    print (num, 'is not divisible by 5 and 11.')
