'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(-1)
        current = dummy
        
        while l1 != None or l2 != None:
            if l1 == None:
                x = 0
            else:
                x = l1.val
            if l2 == None:
                y = 0
            else:
                y = l2.val
            
            digitSum = x + y + carry
            carry = digitSum // 10
            current.next = ListNode(digitSum % 10)
            current = current.next
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        
        if carry == 1:
            current.next = ListNode(1)
            
        return dummy.next
        
        



