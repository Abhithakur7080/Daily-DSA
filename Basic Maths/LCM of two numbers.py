"""
You are given two integers n1 and n2. You need find the Lowest Common Multiple (LCM) of the two given numbers. Return the LCM of the two numbers.

The Lowest Common Multiple (LCM) of two integers is the lowest positive integer that is divisible by both the integers.

Example 1
Input: n1 = 4, n2 = 6
Output: 12

Explanation: 4 * 3 = 12, 6 * 2 = 12.
12 is the lowest integer that is divisible both 4 and 6.
"""

class Solution:
    def LCM(self, n1, n2):
        a, b = n1, n2
        while b != 0:
            a, b = b, a%b
        gcd = a
        return (n1 * n2)//gcd

if __name__ == "__main__":
    n1 = int(input().strip())
    n2 = int(input().strip())
    obj = Solution()
    print(obj.LCM(n1, n2))