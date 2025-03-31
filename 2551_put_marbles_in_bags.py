from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        # Idea: loop through all weights, try to partition at every index, and 
        # store the cost of partitioning at that index (cost = cost of left bag + cost of right bag)

        # Then, put all the costs into a PQ and take min(k) and max(k)

        # If len(weights) == 1, then return itself
        if len(weights) == 1 or k == 1:
            return 0

        # Partition costs start with the left and right most partitions
        partition_costs = []

        # 1. Try partitions, left inclusive
        for i in range(len(weights) - 1):
            left_cost = weights[0] + weights[i]
            right_cost = weights[i + 1] + weights[-1]

            # Append partition cost
            partition_costs.append(left_cost + right_cost)

        # 2. Sort the partitions, and take min k-1 and max k-1
        partition_costs.sort()

        min_costs = partition_costs[:k-1]
        max_costs = partition_costs[-(k-1):]

        return sum(max_costs) - sum(min_costs)

    
# print(Solution().putMarbles(weights = [1,3,5,1], k = 2))
# print(Solution().putMarbles(weights = [1, 3], k = 2))
# print(Solution().putMarbles(weights = [25,74,16,51,12,48,15,5], k = 1))