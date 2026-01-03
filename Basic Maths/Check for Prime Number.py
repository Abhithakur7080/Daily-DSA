"""
You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.

A prime number is a number which has no divisors except 1 and itself.

Example 1
Input: n = 5
Output: true

Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.
"""

class Solution:
    def isPrime(self, n):
        if n==1:
            return False
        i=2
        while i*i<=n:
            if n%i == 0:
                return False
            i+=1
        return True

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.isPrime(n))