def solve(n):
    if n == 0: return 0
    nums = [0] * (n+1)
    nums[1] = 1
    for i in range(2, n+1):
        nums[i] = nums[i//2] + nums[i//2+1] * (i % 2)
    return max(nums)

if __name__ == "__main__":
    print(solve(0))
    print(solve(11))
