class Solution:
    def numOfSubarrays(self, arr) -> int:
        
        # Start from subarrays which include the first number - O(n),
        # calculate the number of subarrays that are even and odd

        # For each subsequence number:
        # if n is even, remove 1 from even count
        # if n is odd, remove 1 from odd count and swap the number of even and odd subarrays

        # then use a sum to sum up all odd subarrays

        # Initial loop
        total = 0
        curr_odd_subarrays = 0
        curr_even_subarrays = 0

        for n in arr:
            total += n

            # If total is odd, add to total odd subarrays, else add to total_even
            if total % 2 == 1:
                curr_odd_subarrays += 1
            else:
                curr_even_subarrays += 1

        # Sum up all odd subarrays
        total_odd_subarrays = curr_odd_subarrays

        # Loop through each number,
        # if number is even remove 1 from even count,
        # if number is odd remove 1 from odd count and swap even and odd subarrays
        for n in arr:
            if n % 2 == 0:
                curr_even_subarrays -= 1
            else:
                curr_odd_subarrays -= 1
                
                # Swap
                curr_odd_subarrays, curr_even_subarrays = curr_even_subarrays, curr_odd_subarrays

            # Add to total
            total_odd_subarrays += curr_odd_subarrays

        # Return total
        return total_odd_subarrays % (10** 9 + 7)