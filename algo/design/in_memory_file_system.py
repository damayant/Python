import collections
from typing import List

class FileSystem:

    def __init__(self):
        self.paths = collections.defaultdict(list)   # maps directory path to sorted list of children
        self.files = collections.defaultdict(str)    # maps full file path to its content

    def ls(self, path: str) -> List[str]:
        if path in self.files:
            return [path.split('/')[-1]]
        else:
            return self.paths[path]  # already kept in sorted order via manual insert

    def mkdir(self, path: str) -> None:
        directories = path.split('/')
        for i in range(1, len(directories)):
            current = '/'.join(directories[:i]) or '/'
            child = directories[i]
            if child not in self.paths[current]:
                self._insert_sorted(self.paths[current], child)

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files:
            self.mkdir(filePath)
        self.files[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]

    # --------------------------
    # 🔧 Helper: Insert sorted
    # --------------------------
    def _insert_sorted(self, arr: List[str], value: str):
        """Insert value into list arr keeping it sorted lexicographically (binary search)"""
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < value:
                left = mid + 1
            else:
                right = mid
        arr.insert(left, value)  # insert at correct position

```
| Operation               | Time Complexity    | Space Impact                |
| ----------------------- | ------------------ | --------------------------- |
| `mkdir(path)`           | O(d \* k\_avg)     | O(d) for new directories    |
| `ls(path)`              | O(k)               | No extra space              |
| `addContentToFile()`    | O(d \* k\_avg + c) | O(f + C) for file + content |
| `readContentFromFile()` | O(L)               | No extra space              |
```