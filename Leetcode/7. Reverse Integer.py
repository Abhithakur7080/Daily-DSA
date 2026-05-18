"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321
"""

class Solution:
    def reverse(self, x: int) -> int:
        # check if the number is negative
        isNegative = x<0
        ans = 0
        # take absolute value of the number
        x = abs(x)
        # reverse the number
        while x !=0:
            lastDigit = x%10
            # check if the reversed number is within the 32-bit integer range before multiplying
            if ans > (2**31 - 1)//10:
                return 0
            ans = ans*10 + lastDigit
            x = x//10
        # if the number is negative, make the reversed number negative
        ans = -ans if isNegative else ans
        return ans

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.reverse(n))