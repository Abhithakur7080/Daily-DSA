"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *


Print the pattern in the function given to you.
"""

class Solution:
    def pattern20(self, n):
        rowsLength = 2*n-1
        colsLength = 2*n
        for r in range(1, rowsLength+1):
            stars = 0
            if(r<=n):
                stars = r
            else:
                stars = rowsLength - (r-1)
            spaces = colsLength - 2*stars
            # Iterators
            for s in range(1, stars+1):
                print("*", end="")
            for s in range(1, spaces+1):
                print(" ", end="")
            for s in range(1, stars+1):
                print("*", end="")
            print("")

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern20(n)