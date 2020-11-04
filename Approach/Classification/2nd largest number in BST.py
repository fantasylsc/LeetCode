'''

Find second largest number in BST

if there is no right subtree:
    return find_largest(current.left)
elif current.right and current.right has no children:
    return current
else:
    return find_second_largest(current.right)

'''







