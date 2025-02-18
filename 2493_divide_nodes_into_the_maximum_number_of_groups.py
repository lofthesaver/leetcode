https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

from collections import deque

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        # If two nodes are connected with an edge, they must be in adjacent groups

        # Step 1: create adjList
        adjList = [[] for _ in range(n + 1)]

        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        # Step 2: check if graph is bipartite
        colors = [-1] * (n + 1)
        for v in range(1, n + 1):

            if colors[v] == -1:

                # BFS
                colors[v] = 0
                q = deque()
                q.append(v)

                while q:
                    curr_vertex = q.popleft()
                    
                    for neighbor in adjList[curr_vertex]:

                        if colors[neighbor] == -1:
                            colors[neighbor] = 1 - colors[curr_vertex]
                            q.append(neighbor)

                        elif colors[curr_vertex] == colors[neighbor]:
                            return -1  


        # Step 3: find all components
        components = []
        visited = [0] * (n + 1)
        for v in range(1, n + 1):

            if visited[v]:
                continue

            # If not visited, create new component
            if not visited[v]:
                new_component = []

            # BFS from this vertex
            q = deque()
            q.append(v)

            while q:
                curr_vertex = q.popleft()
                if visited[curr_vertex]:
                    continue
                
                new_component.append(curr_vertex)
                visited[curr_vertex] = 1

                for neighbor in adjList[curr_vertex]:
                    q.append(neighbor)

            # After one loop, append the new component to components array
            components.append(new_component)


        # # Step 4: loop through all components,
        # # for each component try all vertices and get the largest value
        max_levels = [0] * len(components) # record max level of each component
        print("components: ", components)
        for i, component in enumerate(components):
            
            component_level = 0

            for v in component:

                # BFS
                visited = [0] * (n + 1)

                # Use array to keep track of the level of this vertex
                levels = [-1] * (n + 1)
                q = deque()
                q.append(v)

                # Record level
                levels[v] = 1

                while q:
                    curr_vertex = q.popleft()
                    
                    if visited[curr_vertex]:
                        continue

                    # Set this vertex to visited
                    visited[curr_vertex] = 1

                    # if this vertex has unvisited neighbors, add 1 to levels
                    # and add neighbors to queue
                    neighbors = adjList[curr_vertex]

                    # Find unvisited neighbors
                    unvisited_neighbors = []
                    for neighbor in neighbors:
                        if visited[neighbor] == 0:
                            unvisited_neighbors.append(neighbor)

                    # If there are unvisited neighbors, add 1 to total level and add neighbors to queue
                    for neighbor in unvisited_neighbors:
                        # Set level of neighbor to 1 + level of curr vertex
                        levels[neighbor] = levels[curr_vertex] + 1
                        q.append(neighbor)

                # Record component level
                component_level = max(max(levels), component_level)

            max_levels[i] = component_level

        return sum(max_levels)