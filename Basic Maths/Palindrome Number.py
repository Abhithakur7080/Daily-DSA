"""
You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.

A palindrome number is a number which reads the same both left to right and right to left.

Example 1
Input: n = 121
Output: true

Explanation: When read from left to right : 121.
When read from right to left : 121.
"""

class Solution:
    def reversedNumber(self, n):
        result = 0
        while(0<n):
            lastNum = n%10
            result = result*10 + lastNum
            n = n//10
        return result
    def isPalindrome(self, n):
        return n == self.reversedNumber(n)

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.isPalindrome(n))