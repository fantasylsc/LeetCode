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
        
