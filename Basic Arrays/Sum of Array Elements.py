"""
Given an array arr of size n, the task is to find the sum of all the elements in the array.

Example 1
Input: n=5, arr = [1,2,3,4,5]
Output: 15

Explanation: Sum of all the elements is 1+2+3+4+5 = 15
"""
class Solution:
	def sum(self,arr, n): 
         sum_array = 0
         for i in range(n):
             sum_array = sum_array + arr[i]
         return sum_array
	
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    obj = Solution()
    print(obj.sum(arr, n))