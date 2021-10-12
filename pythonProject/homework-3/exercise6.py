#tax and tip

mealCost =float(input('Enter the cost of the meal: '))

def tipTotal (I1):
    mealCost * .18
    return



#tipTotal = (mealCost*.18)
#print('Your tip amount is: $ ', format (tipTotal, ',.2f'))

taxTotal = (mealCost*.825)
print ('Your tax amount is: $ ', format(taxTotal,',.2f'))

totalCostMeal = mealCost + taxTotal
print ('The cost for you meal plus tax and tip is: $ ',format(totalCostMeal, ',.2f'))

