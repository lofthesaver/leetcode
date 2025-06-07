from collections import deque

class Solution:
    def clearStars(self, s: str) -> str:

        res = list(s)

        # 1. Make a list of 26 stacks
        char_stacks = []
        for i in range(26):
            char_stacks.append(deque())

        # 2. Loop through characters
        for i, c in enumerate(s):

            # If c is not star then add the index of the character to its corresponding stack
            if c != "*":
                char_stacks[ord(c) - ord("a")].append(i)

            # If c is star then remove the last index from the smallest non-empty stack
            elif c == "*":

                # Find smallest non-empty stack
                for stack in char_stacks:
                    if stack:
                        index = stack.pop()

                        # Mark this character as used
                        res[index] = ""
                        break


        # Return string with all characters that is not star
        return "".join(c for c in res if c != "*")
    

print(Solution().clearStars(s = "aaba*"))
print(Solution().clearStars(s = "abc"))