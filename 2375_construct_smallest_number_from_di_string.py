class Solution:
    def smallestNumber(self, pattern: str) -> str:

        # Keep track of current values
        possible_values = set((i for i in range(1, 10)))
            
        def backtrack(stack):
            # print(stack)

            # If solution is satisfied, return True
            if len(stack) == len(pattern) + 1:
                return True

            # Iterate through all possible candidates
            for value in possible_values:

                # If the value is already in the stack, continue
                if value in stack:
                    continue

                # Extract current index and the corresponding pattern
                curr_index = len(stack) - 1
                curr_letter = pattern[curr_index]

                # Check if next candidate is valid -
                # next candidate is valid if the stack is empty,
                # or if the current value is not in stack AND satisfies the pattern
                if not stack or (curr_letter == "I" and value > stack[-1]) or (curr_letter == "D" and value < stack[-1]):

                    # Place next candidate
                    stack.append(value)

                    # Recursively call backtrack with new candidate, until a solution is reached
                    if backtrack(stack):
                        return "".join(str(v) for v in stack)

                    # Remove candidate to backtack and try other possibilities
                    stack.pop(-1)

            # Solution for this recursive branch not reached, return False
            return False
                    
        return backtrack([])
    

# print(Solution().smallestNumber("IIIDIDDD"))
# print(Solution().smallestNumber("DDD"))