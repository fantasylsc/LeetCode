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
# when comes to a new node, always go to the left most, then pop, then go to right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [] # initial stack is empty
        current = root
        # 1. with curr, since initial stack is empty 
        # 2. curr is True, right node to be processed; stack is True, left and mid node to be processed 
        
        # if current is not None, in next step stack will not be None either. Then pop.
        # if stack is not empty, of course stack is not empty. Then pop.
        while current or stack: 
            # go to left most node after processing each node
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right # pay attention
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


