import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[\W_]", "", s).lower()
        i, j = 0, len(s) - 1
        while i < len(s):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
