def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) 
    while left < right:
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