"""
You are given an integer n. You need to return the number of digits in the number.

The number will have no leading zeroes, except when the number is 0 itself.

Example 1
Input: n = 4
Output: 1

Explanation: There is only 1 digit in 4.
"""

class Solution:
    def countDigit(self, n):
        if n==0:
            return 1
        count = 0
        while(0<n):
            n = n//10
            count = count + 1
        return count

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.countDigit(n))