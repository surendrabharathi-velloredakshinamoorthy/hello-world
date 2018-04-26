mylist = [1,2,3,4,5,6,7,8,9]
mylist1 = []
def multiple_list():
	for i in range (0 , len(mylist)):
		if( mylist[i] % 2 == 0):
			mylist1.append(mylist[i])

	print(mylist1)

multiple_list()
