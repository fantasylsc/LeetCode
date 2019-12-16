'''

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        # reverse
        # merge
        
        if not head or not head.next:
            return head
        
        mid = self.findMiddle(head)
        
        l2 = mid.next
        mid.next = None
        l1 = head
        
        re_l2 = self.reverse(l2)
        
        self.merge(l1, re_l2)

        
    def findMiddle(self, head): # mid point is mid.next
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def reverse(self, head):
        newHead = None
        
        while head:
            temp = head.next
            head.next = newHead
            newHead = head
            head = temp
            
        return newHead
        
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(0)
        head = dummy
        count = 0
        
        while l1 and l2:
            if count % 2 == 0:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
            count += 1
        if l1:
            head.next = l1
        if l2:
            head.next = l2

            
            
            
    
           
        