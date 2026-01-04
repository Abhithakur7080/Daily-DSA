"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        result = 0
        while x>0:
            lastNum = x%10
            result = result*10 + lastNum
            x = x//10
        return result == temp

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.isPalindrome(n))