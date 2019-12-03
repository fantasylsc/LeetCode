'''

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def setMapping(s):
            dic = {}
            temp = 0
            for c in s:
                if c in dic:
                    continue
                else:
                    dic[c] = temp
                    temp += 1
            return dic
        
        def mapString(s, dic):
            res = []
            for c in s:
                res.append(dic[c])
            return res
        
        dic1 = setMapping(s)
        dic2 = setMapping(t)
        
        return mapString(s, dic1) == mapString(t, dic2)
        
        