from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        # Factorial
        def factorial(n):
            if n == 0:
                return 1
            
            res = 1
            for i in range(1, n + 1):
                res *= i

            return res

        # 1. Use hashmap to store the occurences of each type of domino
        dominoe_counts = {}
        for i, v in dominoes:

            # Add dominoe
            dominoe_counts[(i, v)] = dominoe_counts.get((i, v), 0) + 1

            # Add reverse if i != v
            if i != v:
                dominoe_counts[(v, i)] = dominoe_counts.get((v, i), 0) + 1

        # For each count that is > 1, add count choose 2 to result
        res = 0
        for pair, count in dominoe_counts.items():
            if count > 1:

                # If not double counted
                if pair[0] == pair[1]:
                    res += ((factorial(count)) / ((factorial(count - 2)) * 2)) * 2

                else:
                    res += ((factorial(count)) / ((factorial(count - 2)) * 2))

        return int(res / 2)

print(Solution().numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]]))
print(Solution().numEquivDominoPairs(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]))