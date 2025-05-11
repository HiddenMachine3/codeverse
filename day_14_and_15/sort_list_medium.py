class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        
        if n==0 or n==1:
            return head
        
        arr = [0 for i in range(n)]

        node = head
        i = 0
        while node:
            arr[i] = node.val
            node = node.next
            i += 1
        
        arr.sort()
        node = head
        i = 0
        while node:
            node.val = arr[i]
            node = node.next
            i += 1

        return head

# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         n = 0
#         node = head
#         while node:
#             n += 1
#             node = node.next
        
#         if n==0 or n==1:
#             return head
        
#         curr_start = head
#         for i in range(n-1):
            
#             curr = curr_start.next
#             for j in range(i+1, n):
#                 if curr_start.val > curr.val:
#                     curr_start.val, curr.val = curr.val, curr_start.val
                
#                 curr = curr.next
#                 print(j)

#             curr_start = curr_start.next

#         return head