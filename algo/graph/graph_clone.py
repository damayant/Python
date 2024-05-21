from typing import List


class Solution :
    def findOrder(numCourses:int,prerequisites:List[List[int]])->List[int]:
        result = []
        visit =  set()

        p_map = { i : [] for i in range(numCourses)}
        for  course , prereqs in prerequisites:
            p_map[course].append(prereqs)
        def dfs(course):
            if course in visit :
                return False
            if p_map[course] == []:
                if course not in visit:
                    result.append(course)
                return True
            visit.add(course)
            for p  in p_map[course]:
                if not dfs(p): return False
            visit.remove(course)
            result.append(course)
            p_map[course] = []
        for course in range(numCourses):
            if not dfs(course): return []
        print(result)
        return result
        
        

    findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
