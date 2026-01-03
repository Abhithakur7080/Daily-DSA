"""
You are given an integer n. You need to find out the number of prime numbers in the range [1, n] (inclusive). Return the number of prime numbers in the range.

A prime number is a number which has no divisors except, 1 and itself.

Example 1
Input: n = 6
Output: 3

Explanation: Prime numbers in the range [1, 6] are 2, 3, 5.
"""

class Solution:
    def isPrime(self, n):
        if n==1:
            return False
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True
    def primeUptoN(self, n):
        if n<0 or 1000<n:
            return 0
        i=2
        count=0
        while i<=n:
            primeNo = self.isPrime(i)
            if primeNo:
                count+=1
            i+=1
        return count

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.primeUptoN(n))