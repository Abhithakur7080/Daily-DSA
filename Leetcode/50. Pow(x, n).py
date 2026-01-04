"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        result = 1.0
        while n > 0:
            # If n is odd
            if n % 2 == 1:
                result *= x
            # Square the base
            x *= x
            # Reduce exponent
            n //= 2
        return result

if __name__ == "__main__":
    x = float(input().strip())
    n = int(input().strip())
    obj = Solution()
    print(obj.myPow(x, n))