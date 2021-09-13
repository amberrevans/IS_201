#Arithmatic

import math

a = int(input('Enter a positive number for a: '))
b = int(input('Enter another positive number for b: '))

#sum
sum = a+b
print ('The sum of',a, 'and',b, 'is',sum)

#difference
difference = a-b
print ('The difference of', b,'from',a,'is',difference)

#product
product = a*b
print ('The product of', a, 'and', b, 'is', product)

#quotient
quotient = a//b
print ('The quotient of', a , 'divided by',b,'is',quotient)
#remainder
remainder = a%b
print ('The remainder of', a,'divided by',b, 'is',remainder)

#the result of log10a
result = math.log10(a)
print ('The result of log10a is', math.log10(a))

#the result of a to the power of b
power = a**b
print ('The result of', a,'to the power of', b,'is', power)
