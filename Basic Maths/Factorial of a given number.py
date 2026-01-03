"""
You are given an integer n. Return the value of n! or n factorial.

Factorial of a number is the product of all positive integers less than or equal to that number.

Example 1
Input: n = 2
Output: 2

Explanation: 2! = 1 * 2 = 2.
"""

class Solution:
    def factorial(self, n):
        if n==0:
            return 1
        fact = 1
        while(n!=0):
            fact = fact * n
            n = n-1
        return fact

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.factorial(n))