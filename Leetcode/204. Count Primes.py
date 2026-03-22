"""
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
        return sum(isPrime)

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    print(obj.countPrimes(n))