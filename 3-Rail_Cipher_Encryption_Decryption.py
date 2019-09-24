userString=input("What would you like to decrypt and encrypt?: ")

# function to encrypr the decrypted text
def threeRailEncrypt(plainText):

	# create empty rails
	railOne=""
	railTwo=""
	railThree=""

	# create rails 
	for i in range(0,len(plainText),4):
		railOne=railOne+plainText[i]

	for i in range(1,len(plainText),2):
		railTwo=railTwo+plainText[i]

	for i in range(2,len(plainText),4):
		railThree=railThree+plainText[i]

	return railOne + railTwo + railThree

print()
print("Encrypted version:")
print(threeRailEncrypt(userString))

# function to decrypt the encrypted text
def threeRailDecrypt(cipherText):

	# creating empty rails
	railOne = [' ' for i in range(len(cipherText))]
	railTwo = [' ' for i in range(len(cipherText))]
	railThree = [' ' for i in range(len(cipherText))]
	j = 0

	# storing the values at the correct positions
	for i in range(0, len(cipherText), 4):
		railThree[i] = cipherText[j]
		j += 1
	
	for i in range(1, len(cipherText), 2):
		railTwo[i] = cipherText[j]
		j += 1
		
	
	for i in range(2, len(cipherText), 4):
		railOne[i] = cipherText[j]
		j += 1		
	
	# recollecting the text
	plainText = ''
	for i in range(len(cipherText)):
		if railThree[i] != ' ':
			plainText += railThree[i]
		if railTwo[i] != ' ':
			plainText += railTwo[i]
		if railOne[i] != ' ':
			plainText += railOne[i]
	
	return plainText

print()
print("Decrypted version:")
print(threeRailDecrypt(threeRailEncrypt(userString)))
