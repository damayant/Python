from typing import Dict, List, Optional
import copy

class File:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content
        self.size = len(content)

    def __repr__(self):
        return f"File(name={self.name}, size={self.size})"


class UserStorage:
    def __init__(self, username: str, max_capacity: Optional[int] = None):
        self.username = username
        self.files: Dict[str, File] = {}
        self.max_capacity = max_capacity  # None means unlimited

    def get_total_used_space(self) -> int:
        return sum(file.size for file in self.files.values())

    def add_file(self, filename: str, content: str) -> bool:
        new_file = File(filename, content)
        new_size = self.get_total_used_space() - self.files.get(filename, File("", "")).size + new_file.size

        if self.max_capacity is not None and new_size > self.max_capacity:
            return False  # Capacity limit exceeded

        self.files[filename] = new_file
        return True

    def get_file_content(self, filename: str) -> str:
        if filename not in self.files:
            raise FileNotFoundError(f"'{filename}' not found for user '{self.username}'")
        return self.files[filename].content

    def delete_file(self, filename: str) -> bool:
        if filename in self.files:
            del self.files[filename]
            return True
        return False

    def list_filenames(self) -> List[str]:
        return list(self.files.keys())

    def get_largest_files(self, top_k: int = 1) -> List[str]:
        sorted_files = sorted(self.files.values(), key=lambda f: f.size, reverse=True)
        return [f.name for f in sorted_files[:top_k]]

    def backup_files(self) -> Dict[str, File]:
        return copy.deepcopy(self.files)

    def restore_files(self, backup_data: Dict[str, File]):
        self.files = backup_data

    def merge_storage_from(self, other_storage: 'UserStorage') -> bool:
        for filename, file in other_storage.files.items():
            if not self.add_file(filename, file.content):
                return False  # Merge failed due to capacity
        return True


class CloudStorageSystem:
    def __init__(self):
        self.users: Dict[str, UserStorage] = {}

    def create_user(self, username: str, max_capacity: Optional[int] = None) -> bool:
        if username in self.users:
            return False  # User already exists
        self.users[username] = UserStorage(username, max_capacity)
        return True

    def upload_file(self, username: str, filename: str, content: str) -> bool:
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.users[username].add_file(filename, content)

    def download_file(self, username: str, filename: str) -> str:
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.users[username].get_file_content(filename)

    def delete_file(self, username: str, filename: str) -> bool:
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.users[username].delete_file(filename)

    def list_user_files(self, username: str) -> List[str]:
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.users[username].list_filenames()

    def get_largest_files_for_user(self, username: str, k: int = 1) -> List[str]:
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.users[username].get_largest_files(k)

    def merge_users(self, source_user: str, target_user: str) -> bool:
        if source_user not in self.users or target_user not in self.users:
            raise ValueError("One or both users do not exist.")
        return self.users[target_user].merge_storage_from(self.users[source_user])

    def backup_user_files(self, username: str) -> Dict[str, File]:
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.users[username].backup_files()

    def restore_user_files(self, username: str, backup_data: Dict[str, File]):
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        self.users[username].restore_files(backup_data)
