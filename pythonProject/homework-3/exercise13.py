#self check out machine math


change = int(input('Please enter the amount: '))

print (change//200,'toonies')
change = change%200
print (change//100, 'loonies')
change = change%100
print (change//25, 'quarters')
change = change%25
print (change//10,'dimes')
change = change%10
print (change//5, 'nickles')
change = change%5
print (change//1, 'pennies')
