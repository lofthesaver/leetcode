# Source: https://labuladong.online/algo/en/essential-technique/sliding-window-framework/#overview-of-the-sliding-window-framework

# Pseudocode framework for sliding window algorithm
def slidingWindow(s: str):

    # Use an appropriate data structure to record the data
    # in the window, which can vary depending on the problem
    window = ...

    left, right = 0, 0

    while right < len(s):

        # Determine whether the left side of the window needs to be contracted
        while left < right and window needs shrink:

            # Remove left element from window
            left_elem = s[left]
            window.remove(left_elem)

            # Shrink the window
            left += 1
            
            # Perform a series of updates on the data within the window
            ...

        # Add right element to window
        right_elem = s[right]
        window.add(right_elem)

        # Expand the window
        right += 1

        # Perform a series of updates on the data within the window
        ...

        # *** position for debug output ***
        # Note that you should not print in the final solution code
        # because IO operations are time-consuming and may cause timeouts
        # print(f"window: [{left}, {right})")
        # ***********************