from heapq import heapify, heappop, heappush

# Summary: toposort, but in_degree replaced by out_degree 
# (done by reversing edges of directed graph)\

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        num_of_vertices = len(graph)
        adjList = graph

        # Reverse direction of edges
        adjList = [[] for _ in range(num_of_vertices)]
        for v in range(num_of_vertices):
            for neighbor in graph[v]:
                adjList[neighbor].append(v)

        # Create queue
        pq = []
        heapify(pq)

        # Initialize toposort
        toposort = []

        in_degree = [0] * num_of_vertices
        parent = [-1] * num_of_vertices

        # Record in degree of all vertices
        for v in range(num_of_vertices):
            for neighbor in adjList[v]:
                in_degree[neighbor] += 1

        # Loop through all vertices, add to queue if in_degree is 0
        for v in range(num_of_vertices):
            if in_degree[v] == 0:
                heappush(pq, v)

        # While pq is not empty, pop, explore its neighbor, -1 from its in degree,
        # add to queue if in degree is 0
        while pq:
            v = heappop(pq)
            toposort.append(v)
            for neighbor in adjList[v]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    parent[neighbor] = v
                    heappush(pq, neighbor)

        return sorted(toposort)