'''

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

# None-hashmap

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)
    
    # copy and insert node to current list
    def copyNext(self, head):
        while head:
            newNode = Node(head.val, None, None)
            newNode.random = head.random
            newNode.next = head.next
            head.next = newNode
            head = head.next.next
    
    # copy random pointer
    def copyRandom(self, head):
        while head:
            if head.next.random:
                head.next.random = head.random.next
            head = head.next.next
    
    # recover next pointer for original list and copied list
    def splitList(self, head):
        newHead = head.next
        while head:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next:
                temp.next = temp.next.next
        return newHead
        
        
        

# Hashmap

# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         if not head:
#             return None
        
#         dummy = Node(0, None, None)
#         newHead = dummy # head for new list
#         curr = head
#         dic = {}
        
#         while curr:
#             # if current node in dic
#             if curr in dic:
#                 newNode = dic[curr]
#             else:
#                 newNode = Node(curr.val, None, None) # curr not in dic, create newNode
#                 dic[curr] = newNode # mapping of next pointer nodes
#             newHead.next = newNode # update next pointer for newHead
            
#             if curr.random:
#                 if curr.random in dic:
#                     newNode.random = dic[curr.random]
#                 else:
#                     newNode.random = Node(curr.random.val, None, None)
#                     dic[curr.random] = newNode.random
#             # move newHead and curr node forward
#             newHead = newNode
#             curr = curr.next
            
#         return dummy.next
        

            
        
            
        




