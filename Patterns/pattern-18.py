"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

E 
D E 
C D E 
B C D E 
A B C D E

Print the pattern in the function given to you.
"""

class Solution:
    def pattern18(self, n):
        for i in range(1, n+1):
            for j in range(n-i+1, n+1):
                print(chr(64 + j), end=" ")
            print("")

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern18(n)