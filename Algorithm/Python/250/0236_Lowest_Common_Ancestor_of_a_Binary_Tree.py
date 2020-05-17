'''

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest

node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

                     3
                    / \
                   5   1
                  / \  / \
                 6  2  0  8
                   / \
                  7   4


Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# use left, right, mid to represent whether it contains target

class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        # input: root node. If the subtree started from root contains target, return True, else return False.
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # check if the left branch contains target
            left = recurse_tree(current_node.left)

            # check if the right branch contains target
            right = recurse_tree(current_node.right)

            # check if the current node is the target
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            # It means the current node is the lowest common ancester
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if at least one of the current node, left branch or right branch contains target.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans              
        
        
