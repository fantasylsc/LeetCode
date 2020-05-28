'''

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# related: 108. Convert Sorted Array to Binary Search Tree
# O(n) solution

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.current = head
        size = self.getListLength(head)
        
        return self.formBST(size)
        
    def getListLength(self, head):
        size = 0
        
        while head:
            size += 1
            head = head.next
        
        return size

    def formBST(self, size):
        if size <= 0:
            return None
        
        left = self.formBST(size//2)
        root = TreeNode(self.current.val)
        self.current = self.current.next
        right = self.formBST(size - 1 - size//2)
        
        root.left = left
        root.right = right
        
        return root




# O(NlogN) solution
# pay attention to findMiddle

# class Solution:
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         if not head:
#             return None
        
#         mid = self.findMiddle(head)
#         root = TreeNode(mid.val)
        
#         if head == mid: # Base case when there is one element
#             return root
        
#         right = mid.next
#         root.right = self.sortedListToBST(right)
#         left = head
#         root.left = self.sortedListToBST(left)
        
#         return root
        
#     def findMiddle(self, head):
#         prev = None
#         slow = head
#         fast = head
        
#         while fast and fast.next:
#             prev = slow
#             slow = slow.next
#             fast = fast.next.next
        
#         if prev:
#             prev.next = None
        
#         return slow
        
        
        
        
    
    
        
        
        
        
        
        




