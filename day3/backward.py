mylist = "Hello"
def backward():
	backwards = mylist[::-1]
	for i in range (0 , len(backwards)):
		character = backwards[i]
		print (character,)


backward()
