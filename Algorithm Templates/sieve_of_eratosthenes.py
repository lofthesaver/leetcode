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

print(SieveOfEratosthenes(5))
print(SieveOfEratosthenes(13))