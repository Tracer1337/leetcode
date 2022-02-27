def solve(s):
    start, longest, seen = 0, 0, {}
    for i, c in enumerate(s):
        if c in seen and start <= seen[c]:
            start = seen[c] + 1
        else:
            longest = max(longest, i - start + 1)
        seen[c] = i
    return longest

if __name__ == "__main__":
    print(solve("abcabcbb"))
    print(solve("bbbbb"))
    print(solve("pwwkew"))
    print(solve("dvdf"))
