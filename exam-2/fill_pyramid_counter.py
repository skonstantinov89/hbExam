import math

def fill_tetrahedron(num):
	volume = (num**3)/(6*math.sqrt(2))/1000
	# the formula returns ml**3
	return round(volume,2)


def tetrahedron_filled(num, water):
	volumes = []
	for eachEdge in num:
		volumes.append(fill_tetrahedron(eachEdge))

	counter = 0
	isElements = len(volumes)
	while water > 0 and isElements > 0:
		if (water - min(volumes)) >= 0:
			isElements -= 1
			counter +=1
			water -= min(volumes)
			del volumes[volumes.index(min(volumes))]
		else:
			isElements -=1
	return counter



print (tetrahedron_filled([120,20,30], 10))
