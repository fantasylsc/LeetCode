# find the prvious middle node
def findMiddle(self, head):
    prev = None
    slow = head
    fast = head.next
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next





# find the back middle node 
def findMiddle(self, head):
    prev = None
    slow = head
    fast = head
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next



