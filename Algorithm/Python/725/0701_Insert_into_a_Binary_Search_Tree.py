'''

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
# only insert at leaf node
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # leaf node, insert TreeNode
        if not root:
            return TreeNode(val)

        # search insert position
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

# Iteration
# Different from tree traverse, without using stack

# class Solution:
#     def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#         node = root
#         while node:
#             # insert into the right subtree
#             if val > node.val:
#                 # insert right now
#                 if not node.right:
#                     node.right = TreeNode(val)
#                     return root
#                 else:
#                     node = node.right
#             # insert into the left subtree
#             else:
#                 # insert right now
#                 if not node.left:
#                     node.left = TreeNode(val)
#                     return root
#                 else:
#                     node = node.left
#         return TreeNode(val)
    
    
    
    




