"""
Given an array of n elements. The task is to return the count of the number of odd numbers in the array.

Example 1
Input: n=5, array = [1,2,3,4,5]
Output: 3

Explanation: The three odd elements are (1,3,5).
"""

class Solution:
    def countOdd(self, arr, n):
        # initialize count to 0
        count = 0
        # iterate through the array
        for i in range(n):
            # check if the current element is odd
            if arr[i]%2 != 0:
                # increment the count if the current element is odd
                count += 1
        # return the count of odd numbers
        return count

if __name__ == "__main__":
    # take the size of the array
    print("Enter the size of the array: ", end="")
    n = int(input().strip())
    # take the array elements
    print("Enter the elements of the array: ", end="")
    arr = list(map(int, input().strip().split()))
    obj = Solution()
    # print the result
    print("The count of odd numbers in the array is: ", end="")
    print(obj.countOdd(arr, n))