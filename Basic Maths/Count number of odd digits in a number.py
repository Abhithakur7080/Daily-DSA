"""
You are given an integer n. You need to return the number of odd digits present in the number.

The number will have no leading zeroes, except when the number is 0 itself.

Example 1
Input: n = 5
Output: 1

Explanation: 5 is an odd digit.
"""

class Solution:
    def countOddDigit(self, n):
        count = 0
        while(0<n):
            num = n%10
            if num%2 != 0:
                count = count + 1
            n = n//10
        return count

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.countOddDigit(n))