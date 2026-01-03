"""
You are given an integer n. Return the integer formed by placing the digits of n in reverse order.

Example 1
Input: n = 25
Output: 52

Explanation: Reverse of 25 is 52.
"""

class Solution:
    def reverseNumber(self, n):
        result = 0
        while(0<n):
            lastNum = n%10
            result = result*10 + lastNum
            n = n//10
        return result

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.reverseNumber(n))