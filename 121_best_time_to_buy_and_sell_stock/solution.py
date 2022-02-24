import math

def solve(prices):
    least = math.inf
    best = 0
    for p in prices:
        least = min(least, p)
        best = max(best, p - least)
    return best

if __name__ == "__main__":
    print(solve([7,1,5,3,6,4]))
    print(solve([7,6,4,3,1]))
