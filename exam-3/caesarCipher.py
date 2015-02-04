def caesar_encrypt(string, num):
	newString = ''
	for eachIndex in range(0,len(string)):
		checker = ord(string[eachIndex])			
		if 	checker >= 65 and checker <= 90:
			newString += chr((ord(string[eachIndex])-65+num)%26+65)

		elif checker >= 97 and checker <= 122:
			newString += chr((ord(string[eachIndex])-97+num)%26+97)
		else:
			return 'Non-alphabetical characters'
	return newString


print (caesar_encrypt("bcde", 1))
