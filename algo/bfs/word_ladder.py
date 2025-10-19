from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self,beginWord:str,endWord:str,wordList:List[str])->int:
        #base case
        if endWord not in wordList:
            return 0 

        neighbours = defaultdict(list)
        
        #build neighbour 
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+'*'+word[j+1:]
                neighbours[pattern].append(word)
        
        #find shortest path using neighbours
        visit,q=set([beginWord]),deque([beginWord])
        result = len(q)

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                for j in range(len(word)):
                    pattern = word[:j]+'*'+word[j+1:]
                    for neighbour in neighbours[pattern]:
                        if neighbour not in visit:
                            q.append(neighbour)
                            visit.add(neighbour)
            result+=1
        return 0

sol = Solution()
print(sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))


