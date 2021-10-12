#determine vowel or consonant

letter = input('Enter a character: ')
if letter.lower() in ('a','e','i','o','u'):
    print (letter,'is a vowel.')

elif letter.upper() in ('A','E','I','O','U'):
    print (letter, 'is a vowel.')

else:
    print (letter, 'is a consonant.')
