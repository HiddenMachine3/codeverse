class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        if curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev