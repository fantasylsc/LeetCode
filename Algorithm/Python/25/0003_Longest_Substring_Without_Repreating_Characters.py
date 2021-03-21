'''

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

'''

# use dictionary to record visited
# use enumerate(s) to speed up

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        mp = {}
        i = 0

        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]] + 1, i)

            res = max(res, j - i + 1)
            mp[s[j]] = j

        return res




