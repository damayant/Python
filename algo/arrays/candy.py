from typing import List


class Solution:
    def candy(ratings: List[int]) -> int:
        #first initialise an empty array of 1s for length of ratings arry 
        #as each child will get atleast 1 candy
        candies = [1]*len(ratings)
        
        #now traverse from left to right 
        # to make sure the candies are distributed properly comparing left neighbour
        # leave the 0th element of array as it has no left neightbour
        for i in range(1,len(ratings)) :
            #if left neighbour is smaller then add 1 to the current candy-child
            if ratings[i-1] < ratings[i] :
                candies[i] = candies[i-1]+1 
        
        #now traverse right to left
        #comparing the right neighbour
        #leave the extreme most element ie len(ratings)-1th element as it has no right neighbour
        for i in range(len(ratings)-2,-1,-1):
            #check if the current one is greater than its right neighbour 
            if ratings[i] > ratings[i+1]:
                #only choose the heigher of the current and increased
                candies[i] = max(candies[i],candies[i+1]+1)
        
        return sum(candies)