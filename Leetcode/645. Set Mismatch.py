"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
"""
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = -1
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                duplicate = abs(nums[i])
            else:
                nums[index] = -nums[index]
        return duplicate
    
    def findMissing(self, nums: List[int]) -> int:
        missing = -1
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
                break
        return missing
    
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = self.findDuplicate(nums)
        missing = self.findMissing(nums)
        return [duplicate, missing]

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    obj = Solution()
    print(obj.findErrorNums(arr))