text = input("Enter the string: \n")
shiftint = int(input("Enter the digit \n"))
textlen = len(text)

def rotationstr(text,shiftint):
	for i in range(0,textlen):
		partword = text[i]
		partword = ord(partword)
		shiftword = partword + shiftint
		shiftwordtxt = chr(shiftword)
		print(shiftwordtxt , end = '')	


rotationstr(text,shiftint)
