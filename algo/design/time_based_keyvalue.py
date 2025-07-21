from collections import defaultdict

class TimeMap:
    def __init__(self):
        #initialise the store:key-->[(timestamp, value)]
        self.store=defaultdict(list)

    def set(self,key:str,value:str,timestamp:int)->None:
        #store the value with the given timestamp for the key
        self.store[key].append((timestamp,value))

    def get(self,key:str,timestamp:int)->str:
        #if the key does not exist, return empty string
        if key not in self.store:
            return ""
        
        #get the list of (timestamp, value) pairs for the key
        timestamp_value_pairs=self.store[key]
        
        return self.binary_search(timestamp_value_pairs, timestamp)

    def binary_search(self, pairs, timestamp):
        #binary search to find the most recent timestamp<=target time 
        low,high=0, len(pairs) - 1
        result="" #default value if no pair is found

        while low <= high:
            mid = (low + high) // 2
            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1]
                low = mid + 1  # look for a later timestamp
            else:
                high = mid - 1
        return result
        
# Example usage:
if __name__ == "__main__":
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    # print(time_map.get("foo", 1))  # Output: "bar"
    print(time_map.get("foo", 3))  # Output: "bar"
    time_map.set("foo", "bar2", 4)
    print(time_map.get("foo", 4))  # Output: "bar2"
    print(time_map.get("foo", 5))  # Output: "bar2"
    print(time_map.get("foo", 0))  # Output: ""
    print(time_map.get("nonexistent_key", 1))  # Output: ""
