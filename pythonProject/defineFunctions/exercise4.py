#area of a field

def areaOfField ():
    length = float(input('Enter the length of the field in feet: '))
    width = float (input('Enter the width of the field in feet: '))
    area_feet = length*width
    acres = area_feet/43560
    print('The area of the field in feet is: ',area_feet)
    print ('The acreage of the field is: ',format(acres, ',.10f'))
    return
areaOfField()
