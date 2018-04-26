import math
x = 1.5
def test_square_root(x):
	for i in range(1,10):
		y = (x + i/x)/2
		z = math.sqrt(i)
		print(float(i)," \t",y," \t",z,"\t ",(y-z))


test_square_root(x)
