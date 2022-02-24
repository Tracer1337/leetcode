def solve(s, t):
    if len(s) == 0: return True
    i = 0
    for j in range(len(t)):
        if s[i] == t[j]:
            i += 1
        if i == len(s): return True
    return False

if __name__ == "__main__":
    print(solve("abc", "ahbgdc"))
    print(solve("axc", "ahbgdc"))
    print(solve("", "ahbgdc"))
