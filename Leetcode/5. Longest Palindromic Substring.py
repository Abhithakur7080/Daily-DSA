"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""

class Solution:
    def expand(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    def longestPalindrome(self, s: str) -> str:
        longest = "" 
        for i in range(len(s)):
            p1 = self.expand(s, i, i)       # odd
            p2 = self.expand(s, i, i + 1)   # even
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
        return longest

if __name__ == "__main__":
    s = input().strip()
    obj = Solution()
    print(obj.longestPalindrome(s))