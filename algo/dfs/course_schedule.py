from typing import List

class Solution :
    def canFinish(numCourses:int,prerequisites:List[List[int]])->bool:
       #map each course to prerequisite list
       pre_map = { i : [] for i in range(numCourses)}

       visit_set =  set()
       for course , prerqisite in prerequisites :
           pre_map[course].append(prerqisite)

       def dfs(course):
            #base case 1: if already exists in set then loop then the course cannot be completed
           if course in visit_set:
               return False
            #base case 2: this means the prerequisits of this course are checked and it can be completed
           if  pre_map[course] == []:
               return True
         #the course is now added to visit set
           visit_set.add(course)
        #start checking prereqs of the current course in DFS
           for prerqisite in pre_map[course]:
               if not dfs(prerqisite): return False
        #after checking dfs of prereqs when all good remove the current course from visit set
        #and also make the preMap of the course empty signifying that it can be completed 
           visit_set.remove(course)
           pre_map[course] = []
           return True
        
       for course in range(numCourses):
           if not dfs(course):return False
       return True


    print(canFinish(numCourses=5,prerequisites=[[0,1],[0,2],[1,3],[1,4],[3,4]]))
            

       

        

