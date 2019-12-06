'''

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative solution

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        current = root
        
        while current or stack:
            # go to left most node after processing each node
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right
        return res



# Recursive solution

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         self.res = []
#         self.helper(root)
#         return self.res
        
#     def helper(self, root):
#         if not root:
#             return
        
#         if root.left:
#             self.helper(root.left)
#         self.res.append(root.val)
#         if root.right:
#             self.helper(root.right)


