#bottle deposits

def TotalBottleDeposit():
    smallBottles = float(input('Enter the number of bottles one liter or less: '))
    smallBottleDeposit = smallBottles*.10
    print('Your small bottle total is:$', format (smallBottleDeposit,'.2f'))

    largeBottles = float(input('Enter the number of bottles more than one liter:'))
    largeBottleDeposit = largeBottles*.25
    print('Your large bottle deposit is: $ ' , format (largeBottleDeposit, ',.2f'))

    totalDeposit = largeBottleDeposit+smallBottleDeposit
    print('Your total deposit is: $ ', format (totalDeposit,',.2f'))
    return
TotalBottleDeposit()
