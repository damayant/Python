from typing import List

class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes (next characters in words)
        self.children = {}
        # Stores the full word at the end node to mark word completion
        self.word = None  

    def addWord(self, word: str):
        node = self  # Start from the root node
        for char in word:
            # If the character is not in children, create a new TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]  # Move to the next node
        node.word = word  # Store the full word at the last node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build Trie from the list of words
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])  # Get board dimensions
        result = []  # List to store found words

        def dfs(row, col, node):
            char = board[row][col]  # Get current character
            
            # If the character is not in the current Trie node, stop DFS
            if char not in node.children:
                return

            next_node = node.children[char]  # Move to the next Trie node

            # If we have reached the end of a word, add it to result and mark as used
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # Prevent duplicate words from being added

            board[row][col] = '#'  # Mark current cell as visited
            
            # Explore all four directions: down, up, right, left
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc
                # Continue DFS if within bounds of the board
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    dfs(new_row, new_col, next_node)
            
            board[row][col] = char  # Restore original character after DFS
            
            # Optimization: Remove Trie nodes that are no longer needed (prune the Trie)
            if not next_node.children:
                del node.children[char]

        # Step 2: Start DFS from every cell in the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return result  # Return the list of found words
