class Solution:
  def isHappy(self, n: int) -> bool:
    seen = {}
    while n != 1:
      n = self.squareDigits(n)
      if n in seen:
        return False
      seen[n] = True
    return True
  
  def squareDigits(self, n: int) -> int:
    result = 0
    while n > 0:
      digit = n % 10
      result += digit ** 2
      n //= 10
    return result
