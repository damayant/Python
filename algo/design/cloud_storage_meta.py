from typing import Optional


class File:
    def __init__(self,name:str,content:str):
        self.name=name
        self.content=content
        self.size=len(content)
    def __repr__(self):
        return f"File(name={self.name}, size={self.size})"
    

class User:
    def __init__(self,username:str,max_storage:Optional[int]=None):
        self.username=username
        self.files=[]
        self.max_capacity=max_storage 
        

#add/delete/retrive files
def add_file(self,filename:str,content:str)->bool:
    """
    Adds a file to the user's storage.
    Returns True if successful, False if max capacity exceeded.
    """
    new_file=File(filename,content)
    new_size=self.get_total_used_space()-self.files.get(filename)