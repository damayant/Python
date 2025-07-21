from typing import List

class Node:
    def __init__(self):
        self.children = {}           # name -> Node
        self.is_file = False
        self.content = ''            # Only for files

class FileSystem:

    def __init__(self):
        self.root = Node()

     # 📂 List files or directories in the given path
    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)# Navigate to the node at the given path
        if node.is_file: # If it's a file, return just the file name
            return [path.split('/')[-1]]
        # If it's a directory, return a sorted list of its contents (child names)
        return sorted(node.children.keys())
    
    def mkdir(self, path: str) -> None:
        self._traverse(path, create=True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._traverse(filePath, create=True)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._traverse(filePath)
        if not node.is_file:
            raise ValueError("Not a file")
        return node.content

    # --------------------------
    # 🔧 Helper: Traverse
    # --------------------------
    def _traverse(self, path: str, create=False) -> Node:
        node = self.root
        if path == "/":
            return node
        parts = path.strip("/").split("/")
        for part in parts:
            if part not in node.children:
                if create:
                    node.children[part] = Node()
                else:
                    raise FileNotFoundError(f"Path '{path}' not found")
            node = node.children[part]
        return node

# Example usage:
fs = FileSystem()
fs.mkdir("/a/b/c")
fs.addContentToFile("/a/b/c/d.txt", "Hello")
print(fs.ls("/a/b/c"))  # Output: ['d.txt']
print(fs.readContentFromFile("/a/b/c/d.txt"))  # Output: 'Hello'
fs.addContentToFile("/a/b/c/d.txt", " World")
print(fs.readContentFromFile("/a/b/c/d.txt"))  # Output: 'Hello World'
fs.mkdir("/a/b/c/x.txt")
print(fs.ls("/a/b/c"))  # Output: ['d.txt', 'x.txt']
fs.mkdir("/x/y/z")
print(fs.ls("/x/y"))  # Output: ['z']