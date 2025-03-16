import math

class Solution:
    def repairCars(self, ranks, cars: int) -> int:
            
        def can_repair(time):

            # Given a time n, check whether all the cars can be repaired in this time;
            # loop through the mechanics, for each mechanic calculate the maximum number of cars
            # that it can repair in the specified time
            max_cars = 0
            for rank in ranks:
                max_cars += math.floor(math.sqrt(time/rank))
            
            return max_cars >= cars
        
        # Binary search for the minimum time, can_repair checks whether all the cars can be repaired
        # in the given time

        # Min. time is 1, max. time is the time it takes for the mechanic with the maximum rank
        # to repair all the cars

        left, right = 1, max(ranks) * (cars ** 2) # could be [0, n], [1, n] etc. Depends on problem
        while left < right:
            mid = left + (right - left) // 2
            if can_repair(mid):
                right = mid
            else:
                left = mid + 1
        return left


print(Solution().repairCars(ranks = [4,2,3,1], cars = 10))
print(Solution().repairCars(ranks = [5,1,8], cars = 6))