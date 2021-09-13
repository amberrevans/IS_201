#compound interest

deposit = float(input('Enter the amount you wish to deposit into the savings account: '))
print('You entered: $',format(deposit, ',.2f'))

Amount1 = deposit*(1+(.04/1)**1*1)
print ('Your savings balance after one year: $',format(Amount1,'.2f'))

Amount2 = deposit*(1+(.04/1)**1*2)
print ('Your savings balance after two years: $ ',format(Amount2,'.2f'))

Amount3 = deposit*(1+(.04/1)**1*3)
print ('Your savings balance after three years: $ ',format(Amount3,'.2f'))
