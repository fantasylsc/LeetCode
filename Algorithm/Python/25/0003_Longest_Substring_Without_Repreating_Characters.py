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
        visited = {}
        max_len = 0
        start = -1
        
        for i in range(len(s)):
            if s[i] in visited:
                start = max(start, visited[s[i]])
            max_len = max(max_len, i - start)
            visited[s[i]] = i
            
        return max_len




