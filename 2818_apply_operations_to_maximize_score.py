from typing import List

class Solution:
    MOD = int(1e9 + 7)

    def maximumScore(self, nums: List[int], k: int) -> int:
            
        def SieveOfEratosthenes(n):
            """
            Finds all prime numbers from 2 to n, inclusive of n
            """

            # Initiate boolean array to keep track of primes
            prime = [True for i in range(n + 1)]
            p = 2
            while (p * p <= n):

                # If prime[p] is not changed, then it is a prime
                if (prime[p] == True):

                    # Update all multiples of p
                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1

            return [i for i in range(2, n + 1) if prime[i] == True]
        
                # Helper function to compute the power of a number modulo MOD
        
        def _power(base, exponent):
            res = 1

            # Calculate the exponentiation using binary exponentiation
            while exponent > 0:

                # If the exponent is odd, multiply the result by the base
                if exponent % 2:
                    res = (res * base) % self.MOD

                # Square the base and halve the exponent
                base = (base * base) % self.MOD
                exponent //= 2

            return res
        
    
        
        # Step 1: find prime scores of each number
        # Use sieve of eratosthenes to find all primes from 2 to max(nums),
        # then for each number, iterate through its prime factors and divide until the factor is gone
        prime_scores = [0] * len(nums)
        all_primes = SieveOfEratosthenes(max(nums))

        for i, v in enumerate(nums):
            curr_score = 0
             
            #  Loop through all prime numbers
            for prime_num in all_primes:
                
                # Break if it exceeds num
                if prime_num ** 2 > v:
                    break

                # If prime_num is a factor of v, then divide until factor is gone and increment score
                if v % prime_num == 0:
                    curr_score += 1

                    while v % prime_num == 0:
                        v = v // prime_num

            # Score += 1 if the remaining number greater than 1 (prime number left)
            if v > 1:
                curr_score += 1

            # Set score 
            prime_scores[i] = curr_score



        # Step 2: use a monotonic (decreasing) stack to create two arrays:
        # 1) next_dominant, where next_dominant[i] indicates the index of the next dominant element
        # after index i (dominant = has a larger prime score) --> update when popping
        # 2) previous_dominant, where previous_dominant[i] indicates the index of the previous dominant
        # element after index i --> update when pushing, if the stack is not empty

        monotonic_stack = [] # start from 1st pair already inside
        next_dominant = [len(nums)] * len(nums)
        previous_dominant = [-1] * len(nums)

        # Loop through prime scores
        for i, prime_score in enumerate(prime_scores):

            # POP: While previous element has a lower prime score, pop the previous element,
            # and update the next_dominant value of the previous element
            while monotonic_stack and monotonic_stack[-1][1] < prime_score:
                prev_elem = monotonic_stack.pop()
                
                # Update next_dominant of previous element using index
                next_dominant[prev_elem[0]] = i


            # PUSH: if stack is not empty, then update previous_dominant,
            # and push the current element to stack
            if monotonic_stack:
                prev_elem = monotonic_stack[-1]
                previous_dominant[i] = prev_elem[0]

            # Push current element onto stack
            monotonic_stack.append((i, prime_score))

        
        # 3. Calculate the number of subarrays where each number is the dominant element 
        num_of_subarrays = [0] * len(nums)
        for i in range(len(nums)):
            num_of_subarrays[i] = (next_dominant[i] - i) * (i - previous_dominant[i])


        # 4. Sort elements by decreasing value - for each value, perform operations according to the number of subarrays,
        # then move on to the next element
        sorted_elements = sorted(enumerate(nums), key = lambda x: -x[1])

        # Keep track of final score and index of current value
        final_score = 1
        elem_index = 0

        # Perform k operations - Each operation multiplies the score by the element, num_of_subarrays[i] times
        while k > 0:
            num_index = sorted_elements[elem_index][0]
            num_value = sorted_elements[elem_index][1]
            
            num_of_operations = min(k, num_of_subarrays[num_index])
            final_score *= _power(num_value, num_of_operations) % self.MOD

            elem_index += 1
            k -= num_of_operations

        # Return score modulo 10**9 + 7
        return final_score % (10 ** 9 + 7)


# print(Solution().maximumScore(nums = [60, 15, 420, 2, 40], k = 2))
print(Solution().maximumScore(nums = [8,3,9,3,8], k = 2))
print(Solution().maximumScore(nums = [19,12,14,6,10,18], k = 3))