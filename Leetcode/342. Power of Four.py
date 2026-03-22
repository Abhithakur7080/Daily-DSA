"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:
            return False
        while n!=1:
            if n%4 != 0:
                return False
            n //= 4
        return True

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.isPowerOfFour(n))