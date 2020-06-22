'''

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

'''

# pass temporary result and left digits as parameters

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return ''
        self.dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.res = []
        self.helper('', digits)
        return self.res
        
    def helper(self, current, digits):
        if digits:
            for digit in self.dic[digits[0]]:
                self.helper(current + digit, digits[1:])
        else:
            self.res.append(current)

# DFS, recursion

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.digits = digits
        self.res = []
        self.dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.DFS(0, '')
        return self.res
        
    def DFS(self, level, current):
        if level == len(self.digits):
            self.res.append(current)
            return
        letters = self.dic[self.digits[level]]
        for i in range(len(letters)):
            self.DFS(level + 1, current + letters[i])

# BFS
# '2': 'abc', '3': 'def'
# res = [a,b,c]
# res = [ad,bd,cd] + [ae,be,ce] + [cf,bf,cf]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = ['']
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        for i in range(len(digits)):
            temp = []
            letters = dic[digits[i]]
            for j in range(len(letters)):
                for s in res:
                    temp.append(s + letters[j])
            res = temp
        return res

