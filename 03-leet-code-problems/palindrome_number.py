class Solution:
    def isPalindrome(self, x: int) -> bool:
        return list(str(x))==list(str(x)[::-1])

result = Solution()
print(result.isPalindrome(-121))