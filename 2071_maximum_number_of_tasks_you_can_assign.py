from typing import List
from collections import deque

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:

        # 3. Function to determine whether k tasks can be completed,
        # using the sorted list of tasks and workers
        def can_complete(k):

            curr_pills = pills
            j = 0
            task_list = deque()

            # Loop through each task, starting from largest task
            for i in range(k - 1, -1, -1):

                # Loop through all tasks that can be done, add to deque
                while j < k and tasks[j] <= workers[i] + strength:
                    task_list.append(tasks[j])
                    j += 1
                
                # If no tasks can be done, return False
                if len(task_list) == 0:
                    return False
                
                # If the current minimum worker can do the largest task, remove task
                if workers[i] >= task_list[0]:
                    task_list.popleft()
                
                # Else if the current worker cannot do the task, use a pill
                elif curr_pills > 0:
                    task_list.pop()
                    curr_pills -= 1

                # If no pills and nobody can do the largest task, return False
                else:
                    return False
                
            return True

        # 1. Sort tasks and workers
        tasks.sort()
        workers.sort(reverse = True)

        # 2. Binary search for the maximum k value, such that k tasks can be completed
        # but k + 1 tasks cannot be completed
        left, right = 0, min(len(workers), len(tasks))

        while left < right:
            mid = left + (right - left + 1) // 2

            # Check whether k (mid) tasks can be completed
            if can_complete(mid):
                left = mid
            else:
                right = mid - 1
        
        # After loop, left is the minimum k where k tasks cannot be completed,
        # so return left - 1
        return left


    
print(Solution().maxTaskAssign(tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1))
print(Solution().maxTaskAssign(tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5))
print(Solution().maxTaskAssign(tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10))