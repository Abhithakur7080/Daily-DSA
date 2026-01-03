"""
You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.

The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.

Example 1
Input: n1 = 4, n2 = 6
Output: 2

Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6
Greatest Common divisor = 2.
"""

class Solution:
    def GCD(self, n1, n2):
        while n2!=0:
            n1, n2 = n2, n1 % n2
        return n1

if __name__ == "__main__":
    n1 = int(input().strip())
    n2 = int(input().strip())
    obj = Solution()
    print(obj.GCD(n1, n2))