from collections import deque

class Solution:
    def mostProfitablePath(self, edges, bob, amount) -> int:

        # Get number of nodes
        n = len(edges) + 1

        # Idea: 
        # 1. create adjList
        # 2. DFS from bob, record the path it takes from bob to node 0, mark the nodes
        # that it traversed through with the number of steps it took to get to that node

        # 3. BFS from Alice, store cost it takes to get to each node with array,
        # after BFS return the maximum

        # Create adjList
        adjList = []
        for _ in range(n):
            adjList.append([])

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            
        # Visited array for dfs
        visited = [0] * n

        # Number of moves it takes for bob to reach a certain node
        num_of_moves = [10**6] * n

        # Keep track of end nodes
        end_nodes = []

        # Set found variable to break out of dfs if 0 is found
        found = [False]

        # parent[n] = parent of n
        parent = [-1] * n

        # DFS from bob
        def dfs(node):
            if found[0]:
                return

            # If current node is 0, add to path and return
            if node == 0:
                found[0] = True

            # If node not visited, add to path, set to visited, and dfs its neighbors
            if not visited[node]:

                # Set to visited
                visited[node] = 1
                
                # DFS all its neighbors
                for neighbor in adjList[node]:
                    parent[neighbor] = node
                    dfs(neighbor)

        # Run dfs
        dfs(bob)

        # Use parent array to set moves
        curr_moves = 0

        # Starting node
        starting_node = bob

        while starting_node != 0:
            num_of_moves[starting_node] = curr_moves
            starting_node = parent[starting_node]
            curr_moves += 1

        num_of_moves[starting_node] = curr_moves


        # Step 3 - BFS from alice, mark cost it takes to reach all the nodes

        # Initiate visited array
        visited = [0] * n

        # Create array to store cost it takes to reach each node
        cost_to_reach_nodes = [-1] * n

        # Keep track of leaf nodes
        leaf_nodes = []

        # DFS parameters: curr_node, curr_level, curr_cost
        def dfs_alice(curr_node, curr_level, curr_cost):

            # If visited already, return
            if visited[curr_node]:
                return

            # Set to visited
            visited[curr_node] = 1

            # Calculate cost
            if curr_level == num_of_moves[curr_node]:
                new_cost = curr_cost + amount[curr_node] / 2
            elif curr_level < num_of_moves[curr_node]:
                new_cost = curr_cost + amount[curr_node]
            else:
                new_cost = curr_cost

            # Update the cost it takes to reach this node
            cost_to_reach_nodes[curr_node] = new_cost

            # Loop through all neighbors and check whether this is a leaf node
            leaf_node = True
            for neighbor in adjList[curr_node]:
                if not visited[neighbor]:
                    leaf_node = False
                    break
    
            # If leaf node, add to leaf_nodes,
            # else loop through all unvisited neighbors and dfs
            if leaf_node:
                leaf_nodes.append(curr_node)

            else:
                for neighbor in adjList[curr_node]:
                    if not visited[neighbor]:
                        dfs_alice(neighbor, curr_level + 1, new_cost)

        # Call initial dfs
        dfs_alice(0, 0, 0)

        # Loop through all leaf nodes and find the max cost
        max_cost = float("-inf")

        for leaf_node in leaf_nodes:
            max_cost = max(cost_to_reach_nodes[leaf_node], max_cost)

        # Return maximum cost
        return int(max_cost)


# print(Solution().mostProfitablePath(edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]))
# print(Solution().mostProfitablePath(edges = [[0,1]], bob = 1, amount = [-7280,2350]))
# print(Solution().mostProfitablePath(edges = [[0,1],[1,2],[2,3]], bob = 3, amount = [-5644,-6018,1188,-8502]))