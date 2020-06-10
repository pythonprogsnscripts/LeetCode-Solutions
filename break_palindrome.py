# Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes 
# the lexicographically smallest possible string that isn't a palindrome.
# After doing so, return the final string.  If there is no way to do so, 
# return the empty string.

class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        for l in range(len(palindrome) // 2):
            if palindrome[l] != 'a':
                return palindrome[:l] + 'a' + palindrome[l+1:]
        return palindrome[:-1] + 'b' if len(palindrome) > 1 else ""

result = Solution()
print(result.breakPalindrome('abccba'))