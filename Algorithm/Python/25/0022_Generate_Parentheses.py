'''

 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


'''


# backtrack
# think about when to add '(' and when to add ')'
# we can always add '(' when number of '(' is less than n
# we can add ')' when the number of ')' is less than '('

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.backtrack(n, '', 0, 0)
        return self.res
        
    def backtrack(self, n, current, left, right):
        if len(current) == 2 * n:
            self.res.append(current)
            return
        # these two if statement make sure the combination is valid
        if left < n:
            self.backtrack(n, current + '(', left + 1, right)
        if right < left:
            self.backtrack(n, current + ')', left, right + 1)
        
        # Note:
        # this is backtrack because the above two recursions are like:
        # if left < n:
        #     s.append('(')
        #     self.backtrack(n, s , left + 1, right)
        #     s.pop()
        # if right < left:
        #     s.append(')')
        #     self.backtrack(n, s, left, right + 1)
        
