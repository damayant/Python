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


def is_even(num):
	return num%2 == 0

numbers = [1,2,3,4,5,6,7,8,9]

filter_no = filter(is_even,numbers)

print(list(filter_no))
