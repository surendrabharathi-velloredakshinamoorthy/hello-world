a = int(input("Value of a: \n"))
x =2
def square_root(a):
	global x
	while True:	
		print(x)
		y = (x + a/x) / 2
		if (y == x):
		  break;
		x = y

square_root(a)
