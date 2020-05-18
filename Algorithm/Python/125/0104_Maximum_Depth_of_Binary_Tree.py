'''

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recrusion 1

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1
        
        
# Recursion 2
# Recursive tree traversal approach. Track and update maxDpeth of the tree.

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         def traverse(root, depth):
#             if not root:
#                 return
#             if self.max < depth:
#                 self.max = depth
#             traverse(root.left, depth + 1)
#             traverse(root.right, depth + 1)
            
#         self.max = 0
#         traverse(root, 1)
#         return self.max

# Iteration
    
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         stack = []
#         if root:
#             stack.append((1, root))
            
#         depth = 0
#         while stack:
#             curr_depth, root = stack.pop()
#             if root:
#                 depth = max(depth, curr_depth)
#                 stack.append((curr_depth + 1, root.left))
#                 stack.append((curr_depth + 1, root.right))
#         return depth
    
    
