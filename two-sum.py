# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Sol #1 is hashed solution
           : create a hash table of all the elements in the array
           : Time complexity : O(n)
        Sol #2 is brute force attack
           : try all the pairs in the array and see if any of them add up to the target
           : Time complexity : O(n**2)
        '''

        # Sol #1
        d = {}
        for i, n in enumerate(nums):
            if n in d: return (d[n],i)
            d[(target - n)] = i

        # Sol #2    
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]   

result = Solution()
print(result.twoSum([2,7,10,5],7))




