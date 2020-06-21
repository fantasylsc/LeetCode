# find the prvious middle node
# use this function for sorting list
def findMiddle(self, head):
    prev = None
    slow = head
    fast = head.next # if use fast = head, 4->2->1->3, 4->2 endless loop
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    return slow




# find the back middle node 
# use this for convert sorted list to BST
def findMiddle(self, head):
    prev = None
    slow = head
    fast = head 
    # if use head.next, 1->2->3->4
    # mid = 2, left = 1, right = 3->4
    # 3,4, mid = 3 = head(base case condition)
    # return root(3), wrong
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    return slow


