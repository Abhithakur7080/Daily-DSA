"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

1        1
12      21
123    321
1234  4321
1234554321


Print the pattern in the function given to you.
"""

class Solution:
    def pattern12(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end="")
            for j in range(1, 2*(n-i) + 1):
                print(" ", end="")
            for j in range(i, 0, -1):
                print(j, end="")
            print("")

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern12(n)