from typing import List
from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        n = len(edges)

        # 1. Use BFS to find minimum distance between node1 and node2 to all other nodes
        node1_distances = [float("inf")] * n
        node2_distances = [float("inf")] * n

        # BFS
        visited = set()
        queue = deque()
        queue.append((0, node1))

        while queue:

            # Pop
            curr_steps, curr_node = queue.popleft()

            # Set to visited
            visited.add(curr_node)

            # Set distance to this node
            node1_distances[curr_node] = curr_steps

            # Explore neighbors
            neighbor = edges[curr_node]

            # If there is outgoing edge and it has not been visited
            if neighbor != -1 and neighbor not in visited:

                # Add to queue
                queue.append((curr_steps + 1, neighbor))


        # BFS - node2
        visited = set()
        queue = deque()
        queue.append((0, node2))

        while queue:

            # Pop
            curr_steps, curr_node = queue.popleft()

            # Set to visited
            visited.add(curr_node)

            # Set distance to this node
            node2_distances[curr_node] = curr_steps

            # Explore neighbors
            neighbor = edges[curr_node]

            # If there is outgoing edge and it has not been visited
            if neighbor != -1 and neighbor not in visited:

                # Add to queue
                queue.append((curr_steps + 1, neighbor))

        # print(node1_distances)
        # print(node2_distances)


        # 2. Compare to find minimum of all distances 
        min_node = -1
        min_distance = float("inf")

        for i in range(n):
            if max(node1_distances[i], node2_distances[i]) < min_distance:
                min_distance = max(node1_distances[i], node2_distances[i])
                min_node = i

        return min_node


print(Solution().closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))
print(Solution().closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2))