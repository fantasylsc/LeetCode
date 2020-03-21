'''

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# The rule of checking min_depth:
# when comes to a leaf node, update the min_depth
# BFS will stop at a level that has a leaf node
# DFS will traverse through all the nodes in the tree

# BFS

from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        q = deque()
        q.append(root)
        
        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return depth
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

# DFS recursion

# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         if not root.left and not root.right:
#             return 1
        
#         min_depth = float('inf')
#         if root.left:
#             min_depth = min(min_depth, self.minDepth(root.left))
#         if root.right:
#             min_depth = min(min_depth, self.minDepth(root.right))
#         return min_depth + 1

# DFS iterative

# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         min_depth = float('inf')
#         stack = []
#         stack.append((root, 1))
        
#         while stack:
#             node, depth = stack.pop()
#             if not node.left and not node.right:
#                 min_depth = min(min_depth, depth)
#             if node.left:
#                 stack.append((node.left, depth + 1))
#             if node.right:
#                 stack.append((node.right, depth + 1))
#         return min_depth
        
