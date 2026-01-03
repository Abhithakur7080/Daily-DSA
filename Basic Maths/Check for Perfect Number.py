"""
You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.

A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.

Example 1
Input: n = 6
Output: true

Explanation: Proper divisors of 6 are 1, 2, 3.
1 + 2 + 3 = 6.
"""

class Solution:
    def isPerfect(self, n):
        if(n==1):
            return False
        divisor_sum = 1
        i = 2
        while i*i <= n:
            if n%i == 0:
                divisor_sum += i
                if i != n//i:
                    divisor_sum += n//i
            i+=1
        return divisor_sum == n

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.isPerfect(n))