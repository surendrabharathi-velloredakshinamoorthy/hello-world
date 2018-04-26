mylist = [1,2,3,4,5,1]
def has_duplicate():
	for i in range (0,len(mylist)):
		for j in range (0 ,len(mylist)):
			if(i == mylist[j]):
				print("True")
				
			else:
				print("false")
				
		

has_duplicate()
