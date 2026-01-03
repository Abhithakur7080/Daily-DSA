"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********


Print the pattern in the function given to you.
"""

class Solution:
    def pattern19(self, n):
        totalRows = 2*n
        for i in range(1, totalRows+1):
            if(i<=n):
                starRange = n-i+1
                spaceRange = totalRows - 2*starRange
                for j in range(1, starRange+1):
                    print("*", end="")
                for s in range(1, spaceRange+1):
                    print(" ", end="")
                for j in range(1, starRange+1):
                    print("*", end="")
            else:
                starRange = i-n
                spaceRange = totalRows - 2*starRange
                for j in range(1, starRange+1):
                    print("*", end="")
                for s in range(1, spaceRange+1):
                    print(" ", end="")
                for j in range(1, starRange+1):
                    print("*", end="")
            print("")

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern19(n)