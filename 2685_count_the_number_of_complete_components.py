from typing import List
from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        # Make adjList
        adjList = [0] * n
        for node in range(n):
            adjList[node] = []

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        # Count number of fully connected components
        fcc_count = 0

        # BFS, one for each component
        visited = set()
        for node in range(n):

            # If this node has already been visited then skip the BFS
            if node in visited:
                continue

            queue = deque()
            queue.append(node)
            edge_count, node_count = 0, 0
        
            while queue:
                curr_node = queue.popleft()

                if curr_node in visited:
                    continue

                visited.add(curr_node)
                node_count += 1

                # Explore neighbors for this component
                for v in adjList[curr_node]:
                    edge_count += 1
                    queue.append(v)

            # Check if m * (m - 1) / 2 == number of edges / 2
            if node_count * (node_count - 1) / 2 == edge_count / 2:
                fcc_count += 1

        return fcc_count

        
# print(Solution().countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]))
# print(Solution().countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]))