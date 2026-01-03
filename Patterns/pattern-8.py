"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

*********
 *******
  *****
   ***
    *


Print the pattern in the function given to you.
"""

class Solution:
    def pattern8(self, n):
        cols = 2*n-1
        for r in range(1, n+1):
            for c in range(1,cols+1):
                if c < r or cols-r+1 < c:
                    print(" ", end="")
                else:
                    print("*", end="")
            print()

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern8(n)