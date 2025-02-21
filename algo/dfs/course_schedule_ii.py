from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Map each course to its prerequisite list
        pre_map = {i: [] for i in range(numCourses)}
        
        for course, prerequisite in prerequisites:
            pre_map[course].append(prerequisite)

        visit_set = set()  # Set to detect cycles
        order = []  # Stack to store topological order
        visited = set()  # Stores nodes that are fully processed

        def dfs(course):
            if course in visit_set:  # Cycle detected
                return False
            if course in visited:  # Already processed
                return True

            visit_set.add(course)  # Mark as visiting
            for prerequisite in pre_map[course]:
                if not dfs(prerequisite):
                    return False

            visit_set.remove(course)  # Done visiting
            visited.add(course)  # Mark as fully processed
            order.append(course)  # Add to topological order
            return True

        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return []  # If a cycle is detected, return empty list
        
        return order


# Example usage
solution = Solution()
print(solution.findOrder(5, [[0,1],[0,2],[1,3],[1,4],[3,4]]))  



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


