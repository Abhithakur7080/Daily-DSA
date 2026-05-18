"""
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

Example 1
Input: n=5, arr = [1,2,3,4,5]
Output: [5,4,3,2,1]

Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]
"""

class Solution:
    def reverse(self, arr: list, n: int) -> None:
        # initialize two pointers
        left = 0
        right = n-1
        # swap elements from the ends towards the center
        while left<right:
            # swap the elements
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            # move the pointers towards the center
            left += 1
            right -= 1

if __name__ == "__main__":
    # take the size of the array
    print("Enter the size of the array: ", end="")
    n = int(input().strip())
    # take the array elements
    print("Enter the elements of the array: ", end="")
    arr = list(map(int, input().strip().split()))
    obj = Solution()
    # reverse the array
    obj.reverse(arr, n)
    # print the result
    print("The reversed array is: ", end="")
    print(arr)