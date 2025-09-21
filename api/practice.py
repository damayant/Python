from collections import defaultdict
import heapq
import requests

base_url = "https://jsonplaceholder.typicode.com/posts"
filtered_user_array=defaultdict(list)

def get_posts(url):
    response= requests.get(url,timeout=5)
    response.raise_for_status()
    return response.json()

def parse_json(json_array):
    for user in json_array:
        filtered_user_array[user["userId"]].append(user["title"])
    return filtered_user_array

def find_user_with_max_title(filtered_user_array,top):
    heap=[]
    for user in filtered_user_array.keys():
        heapq.heappush(heap,(len(filtered_user_array[user]),user))
        if len(heap)>top:
            heapq.heappop(heap)
    print(heap)

parse_json(get_posts(base_url))
find_user_with_max_title(filtered_user_array,top=3)

