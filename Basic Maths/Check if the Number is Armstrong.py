"""
You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.

An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

Example 1
Input: n = 153
Output: true

Explanation: Number of digits : 3.
13 + 53 + 33 = 1 + 125 + 27 = 153.
Therefore, it is an Armstrong number.
"""

class Solution:
    def calculateSize(self, n):
        size = 0
        while(0<n):
            size = size + 1
            n = n//10
        return size
    def isArmstrong(self, n):
        original = n
        total_sum = 0
        power = self.calculateSize(n)
        while(0<n):
            lastNum = n%10
            total_sum = total_sum + lastNum ** power
            n = n//10
        return total_sum == original

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.isArmstrong(n))

