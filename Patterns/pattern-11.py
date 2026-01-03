"""
Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1

Print the pattern in the function given to you.
"""

class Solution:
    def pattern11(self, n):
        for i in range(n):
            for j in range(i+1):
                num = 1 if (i + j) % 2 == 0 else 0
                print(num, end=" ")
            print("")


if __name__ == "__main__":
    n = int(input().strip())
    obj = Solution()
    obj.pattern11(n)