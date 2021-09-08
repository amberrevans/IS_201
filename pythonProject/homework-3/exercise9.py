#compound interest

deposit = float(input('Enter the amount you wish to deposit into the savings account: '))
print('You entered: $',format(deposit, ',.2f'))

finalAmount1 = deposit*(1+(.04/1))**1*1
print ('Your savings balance after one year: $'format(finalAmount1,'.2f')