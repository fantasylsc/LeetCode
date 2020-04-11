'''

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

               1
              / \
             7   0
            / \
           7  -8

Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q = deque()
        max_level = 0
        max_sum = float('-inf')
        level_sum = 0
        level = 1
        q.append(root)
        
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1
            level_sum = 0
        return max_level
