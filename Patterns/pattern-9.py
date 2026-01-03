"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

Print the pattern in the function given to you.
"""

class Solution:
    def pattern9(self, n):
        for i in range(2*n):
            spaces = 0
            stars = 0
            if i<n:
                spaces = n - i - 1
                stars = 2 * i + 1
            else:
                spaces = i - n
                stars = 2 * (2 * n - i - 1) + 1
            for j in range(spaces):
                print(" ", end="")
            for j in range(stars):
                print("*", end="")
            print()

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern9(n)