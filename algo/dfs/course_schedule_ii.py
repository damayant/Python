from typing import List


class Solution :
    def findOrder(numCourses:int,prerequisites:List[List[int]])->List[int]:
        #map each course to a pre-requisite list
        pre_map = {i : [] for i in range(numCourses)}

        for course , pre in prerequisites :
            pre_map[course].append(pre)

        # a course has 3 possible states:
        # visited -> course has been added to output
        # visiting -> course not added to output but added to cycle
        # unvisited -> course not added to output or cycle

        output = []

        visit , cycle = set(), set()

        def dfs(course):
            if course in cycle: 
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for prerquiste in pre_map[course]:
                if dfs(prerquiste) == False :
                    return False
                
            cycle.remove(course)
            visit.add(course)
            output.append(course)

        
        for course in range(numCourses):
            if dfs(course) == False :
                return []
            # print(output)
        print(output)
        return output
        

    findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
