def solve(nums):
    nums.sort()
    res = set()
    for i, n in enumerate(nums[:-2]):
        seen = {}
        for j, m in enumerate(nums[i+1:]):
            target = (n + m) * -1
            if target in seen:
                newTuple = tuple(sorted([n, m, target]))
                if newTuple not in res:
                    res.add(newTuple)
            seen[m] = j
    return list(res)

if __name__ == "__main__":
    print(solve([-1,0,1,2,-1,-4]))
    print(solve([]))
    print(solve([0]))
    print(solve([0, 0, 0, 0]))
