class Solution:
    def closestPrimes(self, left: int, right: int):

        # For efficiency
        if right - left < 1:
            return [-1, -1]

        if max(2, left) == 2:
            return [2, 3]

        # Run Sieve of Eratosthenes to find all prime numbers in range(left, right + 1)
        primes = [True] * (right + 1)
        
        # Record prime numbers
        prime_numbers = []

        # Start loop from 2
        left_index = 2

        while left_index < len(primes):

            # If current number not prime, continue
            if not primes[left_index]:
                left_index += 1
                continue

            # If current number is prime, add to prime numbers,
            # mark all its multiples as not prime
            if primes[left_index]:

                # If this prime number in range of left, right then add to prime numbers
                if left <= left_index <= right:
                    prime_numbers.append(left_index)

                # Mark multiples to False
                for multiple in range(left_index * 2, right + 1, left_index):
                    primes[multiple] = False

                left_index += 1

        
        # Loop through all prime numbers from left to right + 1 and find smallest pair

        # If only 1 prime, return [-1, -1]
        if len(prime_numbers) < 2:
            return [-1, -1]

        # Set minimum difference
        min_diff = float('-inf')
        curr_res = [prime_numbers[0], prime_numbers[1]]

        # Iteratively check for all pairs (i, j) where j - 1 == 1
        i, j = 0, 1
        while j < len(prime_numbers):
            curr_diff = prime_numbers[j] - prime_numbers[i]
            
            # If the current diff <= 2, then return directly
            if curr_diff <= 2:
                return [prime_numbers[i], prime_numbers[j]]

            # If this difference less than the minimum difference, then set min diff and res to this pair
            if curr_diff < min_diff:
                min_diff = curr_diff
                curr_res = [prime_numbers[i], prime_numbers[j]]

            i += 1
            j += 1

        return curr_res


print(Solution().closestPrimes(10, 19))
print(Solution().closestPrimes(4, 6))
print(Solution().closestPrimes(1, 1))