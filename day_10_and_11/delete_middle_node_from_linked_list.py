class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        if not head.next.next:
            head.next = None
            return head
        
        slow, fast = head, head.next.next

        while fast and fast.next:
            print(slow.val, fast.val)
            fast = fast.next
            if not fast:
                slow = slow.next
                break
            fast = fast.next
            slow = slow.next
            
        
        slow.next = slow.next.next if slow.next else None
        return head