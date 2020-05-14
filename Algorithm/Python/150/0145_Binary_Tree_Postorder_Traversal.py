
'''

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative solution:
# postorder sequence: left, right, root
# using root, right, left traversal, then reverse the result

# Iterative solution 1
# postorder (left, right, root),  use traversal order (root, right, left) and append node reversely

# use deque for queue implementation
from collections import deque

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = deque()
        stack = [root]
        
        while stack:
            current = stack.pop()
            res.appendleft(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return res

        
        
# Iterative solution 2
# Idea: (left, right, root) When we process a node, this node should be left node or its child node was visited

# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
        
#         res = []
#         stack = [root]
#         head = root # record previous visited node
        
#         while stack:
#             t = stack[-1] # t is current node, check whether need to process t or not
#             # if t is a leaf node or t.left or t.right was processed, then process node t
#             if (not t.left and not t.right) or t.left == head or t.right == head:
#                 res.append(t.val)
#                 stack.pop()
#                 head = t # record previous visited node
#             else:
                  # append node to stack
#                 # make sure process left first
#                 if t.right:
#                     stack.append(t.right)
#                 if t.left:
#                     stack.append(t.left)
#         return res
        
        
# Recursive solution:

# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         self.res = []
#         self.helper(root)
#         return self.res
        
#     def helper(self, root):
#         if not root:
#             return
        
#         self.helper(root.left)
#         self.helper(root.right)
#         self.res.append(root.val)
        
        
            
        




