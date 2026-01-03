"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

*****
****
***
**
*

Print the pattern in the function given to you.
"""

class Solution:
    def pattern5(self, n):
        for i in range(n):
            for j in range(n-i):
                print("*", end="")
            print()


if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern5(n)