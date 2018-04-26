mylist = [1,2,3,4,5,6]
newlist = []

def middle():
	for i in range (1, len(mylist) -1):		
		newlist.append(mylist[i])

	print(newlist)

middle()
