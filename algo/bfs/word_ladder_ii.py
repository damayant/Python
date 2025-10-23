from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        # --- Step 1: Build neighbours ---
        neighbours = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbours[pattern].append(word)

        # --- Step 2: BFS to get shortest distance to each word ---
        distance = {beginWord: 0}
        q = deque([beginWord])
        while q:
            word = q.popleft()
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for neighbour in neighbours[pattern]:
                    if neighbour not in distance:
                        distance[neighbour] = distance[word] + 1
                        q.append(neighbour)
        if endWord not in distance:
            return []

        # --- Step 3: Iterative DFS using a stack ---
        res = []
        stack = [(endWord, [endWord])]

        while stack:
            word, path = stack.pop()

            # Base case: reached the beginWord
            if word == beginWord:
                res.append(path[::-1])
                continue

            # For each possible pattern
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                # Move only one level closer
                for neighbour in neighbours[pattern]:
                    if neighbour in distance: #only consider words reachable from beginWord 
                        if distance[neighbour] == distance[word] - 1 :
                            stack.append((neighbour,path+[neighbour]))


        # Deduplicate final results if overlapping paths exist
        unique_res = []
        seen = set()
        for r in res:
            t = tuple(r)
            if t not in seen:
                unique_res.append(r)
                seen.add(t)

        return unique_res
