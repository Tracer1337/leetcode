def solve(n):
    if n == 0: return 0
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    for i in range(10):
        print(i, solve(i))
