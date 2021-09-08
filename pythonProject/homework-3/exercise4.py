#area of a field

length = float(input("Enter the length of the field in feet: "))
print('You entered: ', length, 'feet.')
width = float(input("Enter the width of the field in feet: "))
print('You entered: ', width, 'feet.')

area_feet = length*width
print('The area in square feet is: ', area_feet)

acres = area_feet/43560
print('The acreage of the field is: ', format(acres, ',.10f'))
