class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        # Store all happy strings
        happy_strings = []

        # Initiate possible letters to add
        possible_letters = ('a', 'b', 'c')

        # Optimization - keep track of number of happy strings so far
        counter = [0]
        
        # Backtrack algorithm to generate list of all happy strings of length n
        def backtrack(s):
            # print(s)
            # print(counter[0])

            # Base Case - if candidate is solution, increment count,
            # check if count == k, if it is then return the string,
            if len(s) == n:
                counter[0] += 1

                if counter[0] == k:
                    return s
                else:
                    return False

            # Iterate through all possible candidates
            for next_letter in possible_letters:

                # Check if valid - valid if empty string, or if s[i] != s[i + 1]
                if len(s) == 0 or s[-1] != next_letter:

                    # Place next candidate
                    s += next_letter

                    # Recursively call backtrack with new candidate (if statement added for optimization)
                    found = backtrack(s)
                    if found:
                        return found

                    # Remove candidate to backtrack and try other possibilities
                    s = s[:-1]

                    # Optimization - early break if count[0] > k
                    if counter[0] > k:
                        break

            # for optimization
            return ""

        # Solve
        return backtrack("")
 

# Test Cases
print(Solution().getHappyString(3, 9))
print(Solution().getHappyString(1, 3))
print(Solution().getHappyString(1, 4))