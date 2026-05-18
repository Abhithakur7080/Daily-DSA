"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
from typing import List

class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through the array
        for i in range(len(nums)):
            # Iterate through the array again starting from the next element
            for j in range(i+1, len(nums)):
                # If the sum of the current element and the next element is equal to the target
                # then return the indices of the current element and the next element
                if nums[i] + nums[j] == target:
                    return [i, j]

    # Hashmap Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        # Create a hashmap to store the elements of the array
        # and their indices
        hashmap = {}
        # Store the elements of the array in the hashmap
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        # Check for the complement in the hashmap
        for i in range(len(nums)):
            complement = target - nums[i]
            # If the complement is found in the hashmap and it is not the same element
            # then return the indices of the complement and the current element
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    n = int(input().strip())
    obj = Solution()
    print(obj.twoSumHash(arr, n))