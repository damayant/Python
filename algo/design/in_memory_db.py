from collections import defaultdict
from time import time
from typing import Optional


class InMemoryDB:
    def __init__(self):
        self.store={} # latest value: key -> (value, expiry)
        self.history=defaultdict(list) # key -> list of (timestamp, value, expiry_time)

    def set(self,key:str,value:str,ttl_seconds:Optional[int]=None) -> None:
        expiry_time = None
        now=time.time()
        if ttl_seconds is not None:
            expiry_time = now + ttl_seconds
        self.store[key] = (value, expiry_time)
        self.history[key].append((now, value, expiry_time))

    def get(self,key:str)-> Optional[str]:
        if key not in self.store:
            return None
        value, expiry_time = self.store[key]
        if expiry_time is not None and time.time() > expiry_time:
            del self.store[key]
            return None
        return value
    
    def get_at_time(self, key: str, timestamp: float) -> Optional[str]:
        if key not in self.history:
            return None
        versions=self.history[key]

        #binary search for the latest version before the given timestamp
        low, high = 0, len(versions) - 1
        result = None
        while low <= high:
            mid = (low + high) // 2
            if versions[mid][0] <= timestamp:
                result = versions[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        if not result:
            return None
        value_time,value,expiry=result
        if expiry is not None and timestamp > expiry:
            return None
        return value
