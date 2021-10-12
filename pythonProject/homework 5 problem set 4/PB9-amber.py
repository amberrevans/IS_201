#is alpha, digit, or special character

char = input('Enter a character: ')

if (char.isdigit()):
    print (char, 'is a digit.')

elif (char.isalpha()):
    print (char, 'is an alphabet.')

else:
    print (char, 'is a special character.')
