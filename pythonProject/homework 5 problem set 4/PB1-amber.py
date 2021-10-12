#max of two numbers
a = int(input('Enter a number: '))
b = int(input('Enter a second number: '))

def maximum(a, b):

    if a >= b:
        return a
    else:
        return b
print ('The maximum number is',maximum (a,b))
