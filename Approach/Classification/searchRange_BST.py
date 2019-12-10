'''
Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Print all the keys of tree in range k1 to k2.
Print all the keys in increasing order.

Example:
Input: k1 = 10, k2 = 22, root = Node(20)
Output: 12, 20, 22

                    20
                   /  \
                  8    22
                 / \
                4   12


'''
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def searchRange(root, k1, k2):
    if not root:
        return
    
    if root.val > k1:
        searchRange(root.left, k1, k2)
    if root.val >= k1 and root.val <= k2:
        print(root.val)
    if root.val < k2:
        searchRange(root.right, k1, k2)

k1 = 10 ; k2 = 25 ; 
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12)

searchRange(root, k1, k2)
        


