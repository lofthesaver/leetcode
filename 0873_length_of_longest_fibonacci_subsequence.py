class Solution:
    def lenLongestFibSubseq(self, arr) -> int:

        # Idea: generate all pairs of numbers (as starting values of fibonacci sequence),
        # for each pair generate the next number until the next number is not in the list,
        # keep track of longest subsequence and return

        # Convert arr values to hashset
        value_set = set(arr)

        # Max length of fibonacci
        max_length = 0

        # Loop through all pairs of numbers, for each pair check next num until next_num is not in value_set
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):

                # Pair values
                v1, v2 = arr[i], arr[j]

                # Current length of sequence
                curr_length = 2

                while v1 + v2 in value_set:

                    # Increment curr length
                    curr_length += 1

                    # Let v1 = v2 and v2 = v1 + v2
                    v1, v2 = v2, v1 + v2

                # If curr_length is 2, skip reassignment
                if curr_length == 2:
                    continue

                # Reassign max length
                max_length = max(max_length, curr_length)

        # Max length must be >= 3, else return 0
        return max_length if max_length >= 3 else 0

print(Solution().lenLongestFibSubseq([1,3,7,11,12,14,18]))