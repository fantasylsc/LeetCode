'''

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# newHead = None
# save head.next, reverse pointer, update newHead, update head

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        newHead = None
        
        while head:
            temp = head.next
            head.next = newHead
            newHead = head
            head = temp
        return newHead
        
        
        
