import math

def solve(x):
    if x == 0: return 0
    r = 0
    s = sign(x)
    x = abs(x)
    l = math.floor(math.log10(x))+1
    for i in range(1, l+1):
        r += x % 10 * (10 ** (l-i))
        x //= 10
    if r > 2**31-1 or -r < -2**31:
        return 0
    return r * s

def sign(x):
    return -1 if x < 0 else 1

if __name__ == "__main__":
    print(solve(123))
    print(solve(-123))
    print(solve(120))
    print(solve(0))
