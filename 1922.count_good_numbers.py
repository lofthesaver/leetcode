class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        # For an integer of length n, there are (n + 1) // 2 even digits
        # and n //2 odd digits

        # There are five types of even indices (0, 2, 4, 6, 8) and
        # four types of odd indices (2, 3, 5, 7)
        # so calculate [5 ** (n + 1) // 2] * [4 ** (n) // 2] % mod
        
        # Fast exponentiation function
        def fast_exponentiation(x, y, mod):
            ret, mul = 1, x
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mul % mod
                mul = mul * mul % mod
                y //= 2
            return ret
        
        return (fast_exponentiation(5, ((n + 1) // 2), mod) * fast_exponentiation(4, (n // 2), mod)) % mod


print(Solution().countGoodNumbers(n = 1))
print(Solution().countGoodNumbers(n = 4))
print(Solution().countGoodNumbers(n = 50))