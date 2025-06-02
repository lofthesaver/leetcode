from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:

        # Assign 1 candy to everyone
        candies = [1] * len(ratings)
        
        # Forward pass: check whether right neighbor greater than
        # current - if greater than + 1 to candy
        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1

        # Backward pass: check whether left neighbor greater than current,
        # if greater than candy of left neighbor is max(candies[i - 1], candies[i] + 1)
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)

        # print(candies)
        return sum(candies)

print(Solution().candy(ratings = [1,0,2]))
print(Solution().candy(ratings = [1,2,2]))