"""
Given an array of n elements. The task is to return the count of the number of odd numbers in the array.

Example 1
Input: n=5, array = [1,2,3,4,5]
Output: 3

Explanation: The three odd elements are (1,3,5).
"""

class Solution:
    def countOdd(self, arr, n):
        count = 0
        for i in range(n):
            if arr[i]%2 != 0:
                count += 1
        return count

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    obj = Solution()
    print(obj.countOdd(arr, n))