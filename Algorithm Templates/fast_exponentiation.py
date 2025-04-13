# Fast exponentiation, used to calculate x ** y % mod
mod = 10 ** 9 + 7

def fast_exponentiation(x, y, mod):
    ret, mul = 1, x
    while y > 0:
        if y % 2 == 1:
            ret = ret * mul % mod
        mul = mul * mul % mod
        y //= 2
    return ret

print(fast_exponentiation(5, 99999, mod))