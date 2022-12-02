# Solution 1: Hashmap

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    n = len(nums)
    counts = {}
    for number in nums:
      if not number in counts:
        counts[number] = 0
      counts[number] += 1
      if counts[number] >= n / 2:
        return number

# Solution 2: Constant Space

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    count = 0
    currentNumber = None
    for number in nums:
      if count == 0:
        currentNumber = number
      count += (1 if number == currentNumber else -1)
    return currentNumber
