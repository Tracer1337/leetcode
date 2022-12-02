class Solution:
  def reverseBits(self, n: int) -> int:
    result = 0
    for i in range(32):
      bit = n & 1
      position = 2 ** (31 - i)
      result += bit * position
      n //= 2
    return result
