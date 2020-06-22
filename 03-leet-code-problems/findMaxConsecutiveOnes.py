from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        seq = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                result = 0
            else:
                result += 1
                seq = max(result,seq)
        return seq

result = Solution()
print(result.findMaxConsecutiveOnes([1,0,1,1,0,1]))