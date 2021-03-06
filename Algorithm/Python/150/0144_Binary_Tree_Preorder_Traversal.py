'''

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative solution
# Preorder traversal is the easiest DFS when using iterative approach
# pop, append value into result, append right, append left

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        res = []
        stack = []
        stack.append(root)
        
        while stack:
            temp = stack.pop()
            res.append(temp.val) # append temp.val not temp
            
            # for preorder traversal, append right first, then left
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return res
                
        
# Recursive solution:

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         self.res = []
#         self.preorder(root)
#         return self.res
        
#     def preorder(self, root):
#         if root == None:
#             return
#         self.res.append(root.val)
#         self.preorder(root.left)
#         self.preorder(root.right)
        
# Divide & Conquer

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if not root:
#             return []
        
#         # Divide
#         left = self.preorderTraversal(root.left)
#         right = self.preorderTraversal(root.right)
        
#         # Conquer
#         res.append(root.val)
#         return res + left + right        
     
