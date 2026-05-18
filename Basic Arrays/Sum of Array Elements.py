"""
Given an array arr of size n, the task is to find the sum of all the elements in the array.

Example 1
Input: n=5, arr = [1,2,3,4,5]
Output: 15

Explanation: Sum of all the elements is 1+2+3+4+5 = 15
"""
class Solution:
	def sum(self,arr, n):
        # initialize sum to 0
         sum_array = 0
         # iterate through the array
         for i in range(n):
             # add the current element to the sum
             sum_array = sum_array + arr[i]
         # return the sum
         return sum_array
	
if __name__ == "__main__":
    # take the size of the array
    print("Enter the size of the array: ", end="")
    n = int(input().strip())
    # take the array elements
    print("Enter the elements of the array: ", end="")
    arr = list(map(int, input().strip().split()))
    obj = Solution()
    # print the result
    print("The sum of the array elements is: ", end="")
    print(obj.sum(arr, n))