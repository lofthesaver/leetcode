# Credit: https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/solutions/6427425/construct-the-lexicographically-largest-valid-sequence-java-python-c-c-100-beats/

class Solution:
    def constructDistancedSequence(self, n: int):

        # If n == 1, return [1]
        if n == 1:
            return [1]

        res = [-1] * (n * 2 - 1)

        # Keep track of used numbers
        used = [False] * (n + 1)

        # Start with first number as n
        res[0] = n
        res[n] = n
        used[n] = True


        # Backtrack using index
        def backtrack(index):
            print(index)

            # Termination Case: If index == len(res)
            if index == len(res):
                return True

            # If index is already filled, go to the next index
            if res[index] != -1:
                return backtrack(index + 1)

            # Idea: loop through all numbers from n to 1,
            # for each number if it is not used, try to add it to the result
            # if possible to add, add and return tRue
            # if not possible to add, skip
            for i in range(n - 1, 0, -1):
                
                # If already used
                if used[i]:
                    continue
                
                # If i = 1, not used, and can fill
                if i == 1:
                    res[index] = i
                    used[i] = True

                # Else if i != -1, not used, and can fill
                elif i != 1:

                    # If can fill (not out of bounds, and next index is not filled yet)
                    if index + i < len(res) and res[index + i] == -1:
                        res[index] = i
                        res[index + i] = i
                        used[i] = True

                    # Else if cannot fill
                    else:
                        continue

                # Backtrack
                if backtrack(index + 1):
                    return True

                # If reach here, it means backtrack(index + 1) was false (which means the next number couldn't be filled),
                # so reset the current number
                else:
                    if i == 1:     
                        res[index] = -1
                        used[i] = False
                    else:
                        res[index] = -1
                        res[index + i] = -1
                        used[i] = False

            # No valid sequence
            return False
                    
        # Start backtrack
        backtrack(1)
        return res