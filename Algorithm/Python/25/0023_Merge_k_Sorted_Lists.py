'''

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# solution by merging 2 lists

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwo(l1, l2):
            dummy = ListNode(0)
            head = dummy
            
            while l1 and l2:
                if l1.val <= l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                head = head.next
                
            if not l1:
                head.next = l2
            if not l2:
                head.next = l1
                
            return dummy.next

        
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = mergeTwo(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None
        
# solution using heap

# import heapq

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         q = []
        
#         for l in lists:
#             while l:
#                 heapq.heappush(q, l.val)
#                 l = l.next
        
#         dummy = ListNode(0)
#         head = dummy
        
#         while q:
#             val =  heapq.heappop(q)
#             head.next = ListNode(val)
#             head = head.next
        
#         return dummy.next


