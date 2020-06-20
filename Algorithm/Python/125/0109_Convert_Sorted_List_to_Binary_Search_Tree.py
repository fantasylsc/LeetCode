'''

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

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

# O(n) solution
# equivalent to inorder traversal

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



# similar topic: 108. Convert Sorted Array to Binary Search Tree
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
#         fast = head # if use head.next, 1->2, slow = head, endless loop
        
#         while fast and fast.next:
#             prev = slow
#             slow = slow.next
#             fast = fast.next.next
#         # save node before slow 
#         # if exits, set to None, disconnect list at prev.next
#         if prev:
#             prev.next = None
        
#         return slow
