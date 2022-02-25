def solve(a, b):
    n = max(len(a), len(b))
    carry = 0
    ans = ""
    for i in range(n):
        ca = int(a[-i-1]) if i < len(a) else 0
        cb = int(b[-i-1]) if i < len(b) else 0
        s = ca + cb + carry
        ans = str(s % 2) + ans
        carry = 1 if s > 1 else 0
    if carry == 1: ans = str(carry) + ans
    return ans

if __name__ == "__main__":
    print(solve("11", "1"))
    print(solve("1010", "1011"))
