def squaroot(x):
	x += 0.0
	if (x==1) or (x==0):
		return x
	i,result = 1.0,1.0
	while(result<x):
		if result == x:
			return result
		i += 0.1
		result = i*i
	return i


print(squaroot(11))
