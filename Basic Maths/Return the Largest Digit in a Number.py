"""
You are given an integer n. Return the largest digit present in the number.


Example 1
Input: n = 25
Output: 5

Explanation: The largest digit in 25 is 5.
"""

class Solution:
    def largestDigit(self, n):
        largest = 0
        while(0<n):
            lastNum = n%10
            largest = max(largest, lastNum)
            n = n//10
        return largest

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.largestDigit(n))