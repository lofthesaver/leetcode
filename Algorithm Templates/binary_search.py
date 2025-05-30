def binary_search(array) -> int:
    
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) 
    while left < right:

        # This mid formula works if finding the minimum left value which satisfies the condition;
        # to find maximum, use mid = left + (right - left + 1) // 2
        mid = left + (right - left) // 2

        if condition(mid):
            right = mid
        else:
            left = mid + 1
            
    return left


# Need to customize three things:
# 1) Initial boundary variables left and right, which should include all possible elements
# 2) Return value - return left (returns minimal k satisfying condition) or return left - 1 
# 3) Design condition function