'''

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        
        # dummy node and head node for each list
        dummy1 = ListNode(0)
        head1 = dummy1
        dummy2 = ListNode(0)
        head2 = dummy2
        
        while head:
            if head.val < x:
                head1.next = ListNode(head.val)
                head = head.next
                head1 = head1.next
            else:
                head2.next = ListNode(head.val)
                head = head.next
                head2 = head2.next
        
        head1.next = dummy2.next
        
        return dummy1.next
        
        
        
