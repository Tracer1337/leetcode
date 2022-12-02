class Solution:
  def titleToNumber(self, columnTitle: str) -> int:
    result = 0
    for i in range(len(columnTitle)):
      char = columnTitle[len(columnTitle) - 1 - i]
      decimal = ord(char) - 64
      position = 26 ** i
      result += decimal * position
    return result
