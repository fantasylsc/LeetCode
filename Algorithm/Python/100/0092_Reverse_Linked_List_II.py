'''

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. find start1 and start2 nodes
# 2. reverse middle segment
# 3. find end1 and end2 nodes
# 4. reorder list, start1.next = end1, start2.next = end2

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m > n or head == None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        head = dummy # when m = 1, premNode
        
        for i in range(m - 1):
            if not head:
                return None
            head = head.next
        
        premNode = head
        mNode = head.next
        nNode = mNode
        postnNode = mNode.next
        
        for i in range(n - m):
            if not postnNode:
                return None
            temp = postnNode.next
            postnNode.next = nNode
            nNode = postnNode
            postnNode = temp
            
        mNode.next = postnNode
        premNode.next = nNode
        
        return dummy.next
        
        
        
        

