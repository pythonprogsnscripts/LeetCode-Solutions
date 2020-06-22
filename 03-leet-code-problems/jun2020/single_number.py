from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = Counter(nums)
        for k,v in enumerate(number):
            if number[v] == 1:
                return v


result = Solution()
print(result.singleNumber([2,2,3,2]))