"""
Given an array arr of size n, the task is to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order. If the array is sorted then return True, else return False.

Example 1
Input: n = 5, arr = [1,2,3,4,5]
Output: True

Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.
"""

class Solution:
    def arraySortedOrNot(self, arr, n):
        # iterate through the array starting from the second element
        for i in range(1, n):
            # check if the current element is smaller than the previous element
            # if the current element is smaller than the previous element, return False
            if arr[i] < arr[i-1]:
                return False
        # if the loop completes without returning False, the array is sorted
        return True

if __name__ == "__main__":
    # take the size of the array
    n = int(input().strip())
    # take the array elements
    arr = list(map(int, input().strip().split()))
    obj = Solution()
    # print the result
    print(obj.arraySortedOrNot(arr, n))