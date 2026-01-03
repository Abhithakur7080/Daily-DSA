"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

ABCDE
ABCD
ABC
AB
A

Print the pattern in the function given to you.
"""

class Solution:
    def pattern15(self, n):
        for i in range(1, n+1):
            for j in range(1, n-i+1+1):
                print(chr(64+j), end="")
            print("")

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern15(n)