
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = ListNode
        while curr:
            if curr.val and head.next.val == curr.val:
                curr.next = head.next.next
            else:
                curr = curr.next
        return head

 
        
