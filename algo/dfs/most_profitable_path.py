from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def mostProfitablePath(self,edges:List[List[int]],bob:int,amount:List[int]):

        #build adjacncy list for tree
        def build_graph(edges:List[List[int]]):
            graph=defaultdict(list)
            for u,v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph  
        
        #step 2: bob's arrival time(dfs)
        def compute_bob_time(node:int,parent:int,time:int,graph,bob_time)->bool:
            #fills bob_node[node] with the time bob reaches this node - reaches True if path to 0 if found
            if node==0: #reached alic's start
                bob_time[node]=time 
                return True
            for nei in graph[node]:
                if nei == parent:
                    continue 
                if compute_bob_time(nei,node,time+1,graph,bob_time):
                    bob_time[node]=time 
                    return True
            return False

        #step 3: alice dfs to maximise profit
        def dfs_alice(node:int,parent:int,time:int,profit:int,graph,bob_time):
            #alice vs bob timing
            if bob_time[node]==float('inf') or time<bob_time[node]:
                profit+=amount[node]
            elif time==bob_time[node]:
                profit+=amount[node]//2
            #else alice gets nothing 

            #leaf node check
            if len(graph[node])==1 and node!=0:
                return profit
            
            #explore children 
            best=float('-inf')
            for nei in graph[node]:
                if nei==parent:
                    continue 
                best=max(best,dfs_alice(nei,node,time+1,profit,graph,bob_time))
            return best 
             
            

        graph=build_graph(edges)
        bob_time=[float('inf')]*len(amount)
        compute_bob_time(bob,-1,0,graph,bob_time)
        return dfs_alice(0,-1,0,0,graph,bob_time)
    


    