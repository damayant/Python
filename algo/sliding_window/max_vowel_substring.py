#Given a string s and an integer k, 
# return the maximum number of vowel letters in any substring of s with length k.
#Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
#example
#Input: s = "abciiidef", k = 3
#Output: 3
#Explanation: The substring "iii" contains 3 vowel letters.
#example
#Input: s = "leetcode", k = 3
#Output: 2
#Explanation: "lee", "eet" and "ode" contain 2 vowels.

class Solution:
    def maxVowels(s:str,k:int)->int:
        vowels = {'a','e','i','o','u'}
        
        #build window of size k and count number of vowels in it
        count = 0
        for i in range(k):
            print(s[i])
            count += int(s[i] in vowels)
        
        answer = count

        #slide the window to right , 
        #focus on the added character and the removed character and 
        #update count record largest count
        for i in range(k,len(s)):
            print(s[i])
            count += int(s[i] in vowels)
            print(s[i-k])
            count -= int(s[i-k] in vowels)
            answer = max(answer,count)

        print(answer)
        return answer

    maxVowels(s='abciiidef',k=3)

    
