#Area of a room

def areaOfaRoom ():
    length = float(input('Enter the length of the room in feet: '))
    width = float (input('Enter the width of the room in feet: '))
    area = length*width
    print('You entered',length,'as the length.')
    print('You entered',width,'as the width.')
    print('The area of the room is', area,'square feet.')
    return
areaOfaRoom()


