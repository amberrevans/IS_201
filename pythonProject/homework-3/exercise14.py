#height in feet, inches, and centimeters

feet = int(input('Enter your height in feet: '))
inches = int(input('Enter the remainder of your height in inches: '))

totalInches = (feet*12)+inches
print ('Your total height in inches is',totalInches)

totalCen = totalInches*2.54
print ('Your total height in centimeters is', totalCen)
