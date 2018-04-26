mylist = [1,2,2]

def sorted_list():
	for i in range (0,len(mylist)):
		if (mylist [i] < mylist [i+1]):
			print("True")
			return True
		else:
			print("False")
			return False


sorted_list()
