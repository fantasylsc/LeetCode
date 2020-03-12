'''

19. Remove Nth Node From End of List
Medium

2257

167

Favorite

Share
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None: # only have head node
            return None
        
        fast = head
        slow = head
        
        for i in range(n):
            fast = fast.next
        if fast == None:  # fast == None means to move first node
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return head

# Variation, handle delete first node
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        start = dummy
        end = dummy
        
        for _ in range(n):
            end = end.next
            
        while end.next:
            start = start.next
            end = end.next
            
        start.next = start.next.next
        
        return dummy.next
        

