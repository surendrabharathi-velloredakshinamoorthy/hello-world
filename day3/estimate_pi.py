from math import factorial as f
from math import sqrt

constant = (2 * sqrt(2)) / 9801

while True:
	k = 0
	total = 0
	top = f(4 * k) * (1103 + (26390 * k) )
	bottom = (f(k)**4) * (396 ** (4 * k))
	quo = top / bottom
	total = total + quo
	if quo < 1e15:
		break
	k = k + 1

result = constant * total
print(result)
