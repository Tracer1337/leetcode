# Solution 1: Call inner function twice

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    def one_way_isomorphic(s, t):
      mapping = {}
      for i in range(len(s)):
        charS, charT = s[i], t[i]
        if not charS in mapping:
          mapping[charS] = charT
        elif mapping[charS] != charT:
          return False
      return True
    return one_way_isomorphic(s, t) and one_way_isomorphic(t, s)

# Solution 2: Keep two dictionaries

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    mapping = {}
    mappedChars = {}
    for i in range(len(s)):
      charS, charT = s[i], t[i]
      if not charS in mapping:
        if charT in mappedChars:
          return False
        mapping[charS] = charT
        mappedChars[charT] = True
      elif mapping[charS] != charT:
        return False
    return True
