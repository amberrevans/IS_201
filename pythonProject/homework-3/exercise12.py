#distance between two points on earth

import math

#input one
lat1 = float(input('Enter the latitude of the first point: '))
lon1 = float(input('Enter the longitude of the first point: '))

#input two
lat2 = float(input('Enter the latitude of the second point: '))
lon2 = float(input('Enter the longitude of the second point: '))

#convert degrees to radians
phi1 = math.radians(lat1)
phi2 = math.radians(lat2)
d_phi = math.radians(lat2-lat1)
d_lambda = math.radians(lon2 - lon1)

#average radius of earth
r= 6371.01

a = ( sin(d_phi/2))**2 = cos(lat1)*cos(lat2)*(sin(d_lambda/2))**2
c = 2 * atan2(sqrt(a),sqrt(1-a))
distance = r *c
print (distance)
