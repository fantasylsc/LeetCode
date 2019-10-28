'''

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_paren = ['(', '[', '{']
        right_paren = [')', ']', '}']
        
        for item in s:
            if item in left_paren:
                stack.append(item)
            if item in right_paren:
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if item == ')' and left != '(':
                    return False
                if item == ']' and left != '[':
                    return False
                if item == '}' and left != '{':
                    return False
                
        if len(stack) != 0:
            return False
        else:
            return True



