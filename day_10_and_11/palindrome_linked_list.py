class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next
        return stack == stack[::-1]