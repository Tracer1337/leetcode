def solve(n):
    if n == 0: return 0
    a, b, c = 0, 1, 1
    for i in range(3, n+1):
        a, b, c = b, c, a+b+c
    return c

if __name__ == "__main__":
    for i in range(5):
        print(i, solve(i))
