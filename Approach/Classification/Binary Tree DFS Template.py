
# Binary Tree DFS Template

# Template 1: traverse
class solution:
    def traverse(root):
        if not root:
            return
        # do something with root
        traverse(root.left)
        # do something with root
        traverse(root.right)
        # do something with root
        
# Template 2: Divide & Conquer
class solution:
    def traversal(root):
        if not root:
            # do something and return
        
        # Divide
        left = traversal(root.left)
        right = traversal(root.right)
        
        # Conquer
        result = Merge from left and right
        return result

            
