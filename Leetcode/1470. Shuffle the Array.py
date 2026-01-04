"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
"""
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Length of the input array
        l = len(nums)

        # Result array initialized with zeros
        ans = [0] * l

        # Pointer for the first half of nums (starts from index 0)
        k = 0

        # i -> even indices in ans
        # j -> odd indices in ans
        i, j = 0, 1

        # Loop until we fill the result array
        while i < l and j < l:
            # Place element from the first half at even index
            ans[i] = nums[k]
            k += 1

            # Place element from the second half at odd index
            ans[j] = nums[n]
            n += 1

            # Move to next even and odd positions
            i += 2
            j += 2

        # Return the shuffled array
        return ans

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    n = int(input().strip())
    obj = Solution()
    print(obj.shuffle(arr, n))