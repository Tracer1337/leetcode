import math

def solve(n):
    if n == 0: return [0]
    ans = [0]*(n+1)
    ans[1] = 1
    for i in range(2, n+1):
        c = 2 ** math.floor(math.log2(i))
        ans[i] = ans[i-c] + 1
    return ans

if __name__ == "__main__":
    print(solve(2))
    print(solve(5))
    print(solve(8))
