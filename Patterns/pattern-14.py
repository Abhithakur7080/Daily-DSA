"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

A
AB
ABC
ABCD
ABCDE

Print the pattern in the function given to you.
"""

class Solution:
    def pattern14(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65+j), end="")
            print("")

if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern14(n)