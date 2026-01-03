"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

*
**
***
****
*****
****
***
**
*

Print the pattern in the function given to you.
"""

class Solution:
    def pattern10(self, n):
        totalRows = 2 * n - 1
        for i in range(totalRows):
            stars = 0
            if i<n:
                stars = i + 1
            else:
                stars = totalRows - i
            for j in range(stars):
                print("*", end="")
            print("")

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern10(n)