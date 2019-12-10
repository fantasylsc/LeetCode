'''

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

           7
          / \ 
         3   15
             / \
            9   20


BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.node = deque()
        self._inorder(root)
        
    def _inorder(self, root):
        if not root:
            return
        if root.left:
            self._inorder(root.left)
        self.node.append(root.val)
        if root.right:
            self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.node.popleft()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.node) != 0


# Controlled Recursion

# class BSTIterator:

#     def __init__(self, root: TreeNode):
#         self.node = []
#         self._inorder_left_most(root)
        
#     def _inorder_left_most(self, root):
#         while root:
#             self.node.append(root)
#             root = root.left
        
#     def next(self) -> int:
#         """
#         @return the next smallest number
#         """
#         curr = self.node.pop()
#         if curr.right:
#             self._inorder_left_most(curr.right)
#         return curr.val

#     def hasNext(self) -> bool:
#         """
#         @return whether we have a next smallest number
#         """
#         return len(self.node) > 0
  
    
    
    
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()




