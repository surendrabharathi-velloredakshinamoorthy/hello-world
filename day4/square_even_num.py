from functools import reduce
def sq_even_num():
	sum1 = 0 
	for i in range (0 , 4):
		if (i % 2 == 0):
			sum1 = sum1 + (i * i)
	print(sum1)


def red_sq_even_num(x):
	return x % 2 == 0 
		

r = filter(red_sq_even_num , [0,4])
print (r)
sq_even_num()
