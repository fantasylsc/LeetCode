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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# There is no need to check depth of other subtrees once we find a unbalanced subtree
# in checkDepth function return -1 if find subtree is not balanced 

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def checkDepth(root):
            if not root:
                return 0
            
            left = checkDepth(root.left)
            if left == - 1:
                return -1
            right = checkDepth(root.right)
            if right == - 1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1
            
        return checkDepth(root) != -1
                
        
# Top down recursion
# This solution has to check the depth of every node until find diff_depth > 1
        
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         def getDepth(root):
#             if not root:
#                 return 0
#             left = getDepth(root.left)
#             right = getDepth(root.right)
#             return max(left, right) + 1

          # Return True if haven't find unbalanced subtree
#         if not root:
#             return True
        
#         if abs(getDepth(root.left) - getDepth(root.right)) > 1:
#             return False
#         return self.isBalanced(root.left) and self.isBalanced(root.right)
        
 
# Bottom up recursion

# class Solution:
#     # Return whether or not the tree at root is balanced while also returning
#     # the tree's height
#     def isBalancedHelper(self, root: TreeNode) -> (bool, int):
#         # An empty tree is balanced and has height -1
#         if not root:
#             return True, -1
        
#         # Check subtrees to see if they are balanced. 
#         leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
#         if not leftIsBalanced:
#             return False, 0
#         rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
#         if not rightIsBalanced:
#             return False, 0
        
#         # If the subtrees are balanced, check if the current tree is balanced
#         # using their height
#         return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        
#     def isBalanced(self, root: TreeNode) -> bool:
#         return self.isBalancedHelper(root)[0]
        
    
    
        
        
        
        
        
        




