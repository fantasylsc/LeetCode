'''

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]



'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root, s, path):
            if not root:
                return
            if not root.left and not root.right and (s + root.val) == sum:
                path.append(root.val)
                ans.append(path[:])
                return
            
            dfs(root.left, s + root.val, path + [root.val])
            dfs(root.right, s + root.val, path + [root.val])
        
        ans = []
        path = []
        dfs(root, 0, path)
        return ans


# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#         self.ans = []
#         self.path = []
#         self.sum = sum
#         self.dfs(root, 0)
#         return self.ans
#     '''
#     whenever use backtrack, if there is an append, there should be a pop.
#     so make sure it's recovered after append
    
#     '''

#     def dfs(self, root, s):
#         if not root:
#             return
#         if not root.left and not root.right and (s + root.val) == self.sum:
#             self.path.append(root.val)
#             self.ans.append(self.path[:])
#             self.path.pop()
#             return
        
#         self.path.append(root.val)
#         self.dfs(root.left, s + root.val)
#         self.dfs(root.right, s + root.val)
#         self.path.pop()


