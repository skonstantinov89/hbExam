import math

def tetrahedron_filled(num, water):
	# http://en.wikipedia.org/wiki/Tetrahedron#Heron-type_formula_for_the_volume_of_a_tetrahedron
	heron ={
	'U': num[0],
	'V': num[1],
	'W': num[2],

	'u': num[0],
	'v': num[1],
	'w': num[2]
	}

	z = (heron['W'] - heron['u'] + heron['v']) * (heron['u'] - heron['v'] + heron['W'])
	
	Z = (heron['v'] - heron['W'] + heron['u']) * (heron['W'] + heron['u'] + heron['v'])

	y = (heron['V'] - heron['w'] + heron['u']) * (heron['w'] - heron['u'] + heron['V'])
	
	Y = (heron['u'] - heron['V'] + heron['w']) * (heron['V'] + heron['w'] + heron['u'])
	
	x = (heron['U'] - heron['v'] + heron['w']) * (heron['v'] - heron['w'] + heron['U'])
	
	X = (heron['w'] - heron['U'] + heron['v']) * (heron['U'] + heron['v'] + heron['w'])


	a = math.sqrt(x*Y*Z)
	b = math.sqrt(y*Z*X)
	c = math.sqrt(z*X*Y)
	d = math.sqrt(x*y*z)

	volume = math.sqrt((b+c+d-a)*(a-b+c+d)*(a+b-c+d)*(a+b+c-d))  / (192*heron['u']*heron['v']*heron['w'])
	print (volume)
	return volume / water


pyramidVolume=int(tetrahedron_filled([120,20,30], 10))
# print (pyramidVolume)