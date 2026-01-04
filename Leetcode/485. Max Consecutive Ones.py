"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
"""
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max_cons = 0
        count = 0
        for num in nums:
            if num==1:
                count+=1
                max_cons = max(max_cons, count)
            else:
                count=0
        return max_cons

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    obj = Solution()
    print(obj.findMaxConsecutiveOnes(arr))