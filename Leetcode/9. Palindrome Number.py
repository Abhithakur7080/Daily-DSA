"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # store the original number
        temp = x
        result = 0
        # reverse the number
        while x>0:
            # get the last digit
            lastNum = x%10
            # add the last digit to the result
            result = result*10 + lastNum
            # remove the last digit from the original number
            x = x//10
        # check if the reversed number is equal to the original number
        return result == temp

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.isPalindrome(n))