# Source: https://labuladong.online/algo/en/essential-technique/sliding-window-framework/#overview-of-the-sliding-window-framework

# Pseudocode framework for sliding window algorithm
def slidingWindow(s: str):

    # Window datastructure
    window = ...

    # Initial window
    left = 0

    # Record result
    res = 0

    # Loop through right index
    for right in range(len(s)):

        # Add right element to window
        right_elem = s[right]
        window.add(right_elem)

        # Determine whether the left side of the window needs to be contracted
        while left <= right and window needs shrink:

            # Remove left element from window
            left_elem = s[left]
            window.remove(left_elem)

            # Shrink the window
            left += 1
            
        # Record result, left is the first index where condition is not satisfied
        res += left
    
    return res