from collections import deque
from typing import List

class Solution :
    def canFinish(numCourses:int,prerequisites:List[List[int]])->bool:
       #map each course to prerequisite list
       pre_map = { i : [] for i in range(numCourses)}

       visit_set =  set()
       for course , prerqisite in prerequisites :
           pre_map[course].append(prerqisite)

       def dfs(course):
           if course in visit_set:
               return False
           if  pre_map[course] == []:
               return True
           visit_set.add(course)
           for prerqisite in pre_map[course]:
               if not dfs(prerqisite): return False
           visit_set.remove(course)
           pre_map[course] = []
           return True
        
       for course in range(numCourses):
           if not dfs(course):return False
       return True


    print(canFinish(numCourses=5,prerequisites=[[0,1],[0,2],[1,3],[1,4],[3,4]]))
            

       

        

