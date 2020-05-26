
'''

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # find middle
        # sort left and sort right
        # merge sorted list
        if not head or not head.next:
            return head
        
        mid = self.findMiddle(head)
        
        list1 = self.sortList(mid.next)
        mid.next = None
        list2 = self.sortList(head)
        
        res = self.mergeList(list1, list2)
        
        return res
        
    def findMiddle(self, head):
        slow = head
        fast = head.next # pay attention: when length of list is even, there is error without next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        return slow
        
    def mergeList(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode(0)
        head = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1# use current node, other than creating new node
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
            
        if list1:
            head.next = list1
        else:
            head.next = list2
            
        return dummy.next

            
            
            
            
