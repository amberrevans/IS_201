#valid triangle by angles

print ('Enter the three angles of your triangle: ')

a = int(input())
b= int(input())
c = int(input())

if ((a + b >c) == 180):
    print ('Your triangle is valid.')
else:
    print ('Your triangle is not valid.')
