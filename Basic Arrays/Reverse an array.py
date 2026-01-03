"""
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

Example 1
Input: n=5, arr = [1,2,3,4,5]
Output: [5,4,3,2,1]

Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]
"""

class Solution:
    def reverse(self, arr: list, n: int) -> None:
        left = 0
        right = n-1
        while left<right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    obj = Solution()
    obj.reverse(arr, n)
    print(arr)