from functools import reduce
def even_num():
	sum = 0
	for i in range(100 , 500 ):
		if(i % 2 == 0):
			sum = sum + i
		"""print(i,sum)"""
	print(sum)

def even_num_reduce():
	sum1 = reduce(lambda x,y: x + y ,range(100,500,2))
	print(sum1)

even_num()
even_num_reduce()
