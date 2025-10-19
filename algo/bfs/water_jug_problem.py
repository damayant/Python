from collections import deque


class Solution:
    def canMeasureWater(self,x:int,y:int,target:int)->bool:
        #base case
        if target>x+y:
            return False 

        q,visit=deque([0]),set()
        steps = [x,-x,y,-y]

        while q:
            current = q.popleft()
            for step in steps:
                total = current+step
                if total == target:
                    return True 
                if total not in visit and 0<=total<x+y :
                    visit.add(total)
                    q.append(total)
        return False 
    
sol = Solution()
print(sol.canMeasureWater(x=3,y=5,target=4))