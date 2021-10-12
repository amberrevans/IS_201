#area and volume of a sphere

import math
def areaVolume ():
    radius = float(input('Enter the radius of the circle: '))
    area = math.pi*radius**2
    print ('The area of the circle is',area)
    volume = (4/3*math.pi*radius**3)
    print ('The volume of the sphere is', volume)
    return

areaVolume()