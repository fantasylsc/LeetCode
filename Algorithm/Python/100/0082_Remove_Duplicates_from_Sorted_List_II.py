'''

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        while head.next and head.next.next:
            if head.next.val == head.next.next.val:
                val = head.next.val
                while head.next and head.next.val == val:
                    head.next = head.next.next
            else:
                head = head.next
        return dummy.next
        
        
# 
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
        
#         dummy = ListNode(0)
#         dummy.next = head
#         pre = dummy
#         start = head
        
#         while start and start.next:
#             if start.val == start.next.val:
#                 value = start.val
#                 while start and start.val == value:
#                     start = start.next
#                 pre.next = start
#             else:
#                 pre.next = start
#                 pre = start
#                 start = start.next
                
#         return dummy.next
        
        
        
        



