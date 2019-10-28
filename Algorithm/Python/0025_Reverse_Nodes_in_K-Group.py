
'''

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None or k == 1:
            return head
        dummy = ListNode(0)
        pre = dummy
        cur = head
        dummy.next = head
        
        i = 1
        while cur:
            if i % k == 0:
                pre = self.reverseOneGroup(pre, cur.next)
                cur = pre.next
            else:
                cur = cur.next
            i += 1
        return dummy.next

                
    def reverseOneGroup(self, pre, next_start):
        last = pre.next
        cur = last.next
        while cur != next_start:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last
        



