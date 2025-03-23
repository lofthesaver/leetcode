from typing import List
import heapq # priority queue

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        # Idea: Modified Diijkstra's Algorithm without visited 

        # 1. Create adjList
        adjList = [0] * n
        for node in range(n):
            adjList[node] = []

        for u, v, w in roads:
            adjList[u].append((v, w))
            adjList[v].append((u, w))

        # 2. Initiate cost array, and pq
        cost = [float('inf')] * n
        cost[0] = 0
    
        pq = [(0, 0)] # first argument is the cost, second argument is the node
        heapq.heapify(pq)

        # Initiate number of ways with minimum cost to get to each nodex
        num_of_ways = [0] * n
        num_of_ways[0] = 1

        # 3. Diijkstra's (modified), explore neighbors and reduce cost while PQ still has elements
        while pq:
            curr_cost, curr_node = heapq.heappop(pq)

            # Check if current cost is up to date
            if curr_cost == cost[curr_node]:

                # Loop through neighbors - if curr_cost + weight <= neighbor cost, then add to pq
                for neighbor_node, neighbor_cost in adjList[curr_node]:

                    # If curr_cost + neighbor_cost is equal to the min cost, update the number of ways to get to this node
                    if curr_cost + neighbor_cost == cost[neighbor_node]:
                        num_of_ways[neighbor_node] = (num_of_ways[curr_node] + num_of_ways[neighbor_node]) % (10 ** 9 + 7)

                    # Else if curr_cost + neighbor_cost < min_cost, number of ways to get to neighbor = number of ways to get to curr_node
                    elif curr_cost + neighbor_cost < cost[neighbor_node]:
                        num_of_ways[neighbor_node] = num_of_ways[curr_node]

                        # Update cost of neighbor, and add to pq
                        cost[neighbor_node] = curr_cost + neighbor_cost # update cost of neighbor node
                        heapq.heappush(pq, (cost[neighbor_node], neighbor_node)) # add neighbor node to pq

        # Return the number of ways to get to n - 1
        return num_of_ways[n - 1]


# print(Solution().countPaths(n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))
# print(Solution().countPaths(n = 2, roads = [[1,0,10]]))
# print(Solution().countPaths(n = 6, roads = [[3,0,4],[0,2,3],[1,2,2],[4,1,3],[2,5,5],[2,3,1],[0,4,1],[2,4,6],[4,3,1]]))