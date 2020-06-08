import itertools
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        final = list(itertools.dropwhile(lambda x:x == "0",str(abs(x))[::-1]))
        temp = "".join(final)
        result = int(temp)

        if x < 0:
            result = -1 * result

        if ((result < -pow(2,31)) or (result > pow(2,31))):
            return 0
        return result 

            

res = Solution()
print(res.reverse(-2147483648))