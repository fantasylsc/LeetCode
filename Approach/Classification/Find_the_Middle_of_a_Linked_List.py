# find the prvious middle node
# use this function for sorting list
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # find middle
        # sort left and sort right
        # merge sorted list
        if not head or not head.next:
            return head
        
        mid = self.findMiddle(head)
        
        # if use mid, 4->2->1->3
        # mid = 2, mid = 1, mid = 1
        # endless loop (head and head.next not None)
        
        list1 = self.sortList(mid.next)
        mid.next = None
        list2 = self.sortList(head)
        
        res = self.mergeList(list1, list2)
        
        return res
        
    def findMiddle(self, head):
        slow = head
        fast = head.next 
        # if use fast = head, 4->2->1->3
        # mid = 1, sort(4,2,1), sort(3)
        # mid = 2, sort(4,2), sort(1)
        # mid = 2, sort(4,2), sort(None)
        # ...... endless loop
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        return slow
          
    def mergeList(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode(0)
        head = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1 # use current node, other than creating new node
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
            
        if list1:
            head.next = list1
        else:
            head.next = list2
            
        return dummy.next




# find the back middle node 
# use this for convert sorted list to BST
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        mid = self.findMiddle(head)
        root = TreeNode(mid.val)
        
        if head == mid: # Base case when there is one element
            return root
        
        right = mid.next
        root.right = self.sortedListToBST(right)
        left = head
        root.left = self.sortedListToBST(left)
        
        return root
        
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
        # save node before slow 
        # if exits, set to None, disconnect list at prev.next
        if prev:
            prev.next = None
        
        return slow


