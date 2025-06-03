from collections import defaultdict,deque
import heapq

class Solution:
    def findCheapestPrice(self,num_cities: int,flight_routes: list[list[int]],source_city: int,destination_city: int,max_stops_allowed: int) -> int:
        #step1: build flight graph
        flight_graph=build_directed_weighted_graph(flight_routes)

        #step 2: apply modified dijkstra algo using min-heap with (cost,current_city,stops)
        return dijkstra_with_stop_constraint(flight_graph,source_city,destination_city,max_stops_allowed,num_cities)
    
def build_directed_weighted_graph(flight_routes: list[list[int]]) :
    flight_graph=defaultdict(list)
    for from_city,to_city,cost in flight_routes:
        flight_graph[from_city].append((to_city,cost))
    return flight_graph

def dijkstra_with_stop_constraint(flight_graph: defaultdict,source_city: int,destination_city: int,max_stops_allowed: int,num_cities: int) -> int:
    #priority queue to store (cost, current_city, stops)
    min_heap = [(0, source_city, 0)]  # (cost, current_city, stops)

    #tracks min stops taken to reach each city
    visited = defaultdict()

    while min_heap:
        cost, current_city, stops = heapq.heappop(min_heap)

        #if we reach destination city, return the cost
        if current_city == destination_city:
            return cost

        #if we have already visited this city with fewer stops, skip it
        if current_city in visited and visited[current_city] < stops:
            continue

        #mark the city as visited with the current number of stops
        visited[current_city] = stops

        #if we can still take more stops, explore neighbors
        if stops <= max_stops_allowed:
            for neighbor, flight_cost in flight_graph[current_city]:
                new_cost = cost + flight_cost
                heapq.heappush(min_heap, (new_cost, neighbor, stops + 1))
    #if we exhaust all options and never reach the destination city, return -1
    return -1

# Example usage:
num_cities = 4
flight_routes = [[0, 1, 100],  # 0 → 1 costs 100
    [1, 2, 100],  # 1 → 2 costs 100
    [0, 2, 500],  # 0 → 2 costs 500
    [2, 3, 100]]
source_city = 0
destination_city = 3
max_stops_allowed = 2
solution = Solution()
print(solution.findCheapestPrice(num_cities, flight_routes, source_city, destination_city, max_stops_allowed))
        