import math

def fill_tetrahedron(num):
	volume = (num**3)/(6*math.sqrt(2))/1000
	# the formula returns ml
	return round(volume,2)

print (fill_tetrahedron(100))
