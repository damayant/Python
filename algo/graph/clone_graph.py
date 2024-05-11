class Node: 
    def __init__(self,val=0,neighbours = None):
        self.val =  val
        self.neighbours = neighbours if  neighbours is not None else []

class Solution :
    def cloneGraph(node:Node)->Node:
        old_to_new = {}

        def dfs(node):
            if  node in  old_to_new :
                return old_to_new
            
            if node is not None:
                copy =  Node(node.val)
                old_to_new[node] = copy

                for n in node.neighbours :
                    copy.neighbours.append(dfs(n))
                return copy

        return dfs(node)

    node_input = Node(val=1,neighbours=[[2,4],[1,3],[2,4],[1,3]])
    print(cloneGraph(node_input))
