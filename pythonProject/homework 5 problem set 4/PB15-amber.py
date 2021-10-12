#valid triangle by sides

def validTriangle (a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

sideA = float(input('Enter the length of side A: '))
sideB= float(input('Enter the length of side B: '))
sideC = float(input('Enter the length of side C: '))

if validTriangle (sideA, sideB, sideC):
    print ('Triangle is valid.')
else:
    print ('Triangle is not valid.')
