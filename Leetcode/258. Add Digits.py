"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
"""

class Solution:
    # Brute Force(nlog(n) - TC)
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num
    # Optimal O(1) - TC
    def addDigits2(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
    # Optimal O(1) - TC
    def addDigits3(self, num: int) -> int:
        if num == 0:
            return 0
        return 1+ (num - 1) % 9