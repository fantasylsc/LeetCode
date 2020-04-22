'''

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.



'''

from collections import Counter
'''
Approach: use a window to track characters. Move right pointer right until the windows has all the elements in t.
Then move left pointer right to contract the window.

formed is used to keep track of how many unique characters in t are present 
in the current window in its desired frequency.
e.g. if t is "AABC" then the window must have two A's, one B and one C. 
Thus formed would be = 3 when all these conditions are met.

'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)
        l, r = 0, 0

        formed = 0
        window_counts = {}
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
        
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1    

            r += 1    

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
                    
            
             
            
        
        
        
        
