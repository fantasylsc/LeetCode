'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0:
            return ''
        
        res = ''
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    return res
            res += strs[0][j]
            
        return res




