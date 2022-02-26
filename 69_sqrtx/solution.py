import math

def solve(x):
    l, r, mid = 0, x, 0
    while l <= r:
        mid = math.floor((l+r)/2)
        sqr = mid*mid
        nextSqr = (mid+1) * (mid+1)
        if sqr <= x and nextSqr > x:
            return mid
        if sqr < x: l = mid + 1
        else: r = mid - 1

if __name__ == "__main__":
    print(solve(0))
    print(solve(4))
    print(solve(9))
    print(solve(40))
