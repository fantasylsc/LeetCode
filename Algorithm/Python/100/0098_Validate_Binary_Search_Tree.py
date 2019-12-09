'''

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validBST(root, minVal, maxVal):
            if not root:
                return True
            
            if root.val <= minVal or root.val >= maxVal:
                return False
            leftRes = validBST(root.left, minVal, root.val)
            rightRes = validBST(root.right, root.val, maxVal)
            
            return leftRes and rightRes
        
        return validBST(root, float('-inf'), float('inf'))



# Iteration

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         stack = [(root, float('-inf'), float('inf'))]
        
#         while stack:
#             node, minVal, maxVal = stack.pop()
#             if node.val <= minVal or node.val >= maxVal:
#                 return False
#             if node.left:
#                 stack.append((node.left, minVal, node.val))
#             if node.right:
#                 stack.append((node.right, node.val, maxVal))
#         return True
                
        


