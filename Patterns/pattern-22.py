"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5

Print the pattern in the function given to you.
"""

class Solution:
    def pattern22(self, n):
        size = 2 * n - 1
        for r in range(1, size+1):
            for c in range(1, size+1):
                rowDirection = abs(r-n)
                colDirection = abs(c-n)
                maxDirection = max(rowDirection, colDirection)
                value = maxDirection + 1
                print(value, end=" ")
            print("")

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern22(n)