'''

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# approach 1 hash

# approach 2 slow fast pointer

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        p1 = self.getIntersection(head)
        if p1 == None:
            return None
        p2 = head
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
        
    def getIntersection(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
    
           
        
