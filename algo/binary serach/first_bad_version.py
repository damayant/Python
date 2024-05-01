# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        mid = 0

        while(start<end):
            mid = (start + end)//2
            #since all versions before a good version are also good ones so move start = mid+1
            if isBadVersion(mid) == False: # type: ignore
                start = mid +1
            else :
                end = mid
        
        return start
        