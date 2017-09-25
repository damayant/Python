__author__ = "Damayanti"
__version__ = "Python 3.6.1 :: Anaconda 4.4.0 (x86_64)"

#find a word in a passage using rabin karp method
def hashing(text):
	sum = 0
	for i in range(len(text)):
		sum += ord(text[i])
	return sum

def pattern_matching(string,substring):
	length, hash = len(substring), hashing(substring)
	for i in range(len(string)-length+1):
		text = string[i:i+length]
		if(hashing(text)==hash):
			return True
	return False

#Driver Function
print(pattern_matching("goodnight","nighty"))

#Complexity :: O(n+m) [average] , n ->no of elements in substring, m ->no of elements in string
