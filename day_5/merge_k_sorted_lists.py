# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def get_min_node():
            first_node = None
            min_val = float('inf')
            min_node = None
            idx = 0
            for i,node in enumerate(lists):
                if node and node.val < min_val:
                    min_val = node.val
                    min_node = node
                    idx = i
            
            return min_node, idx
        first_node, i = get_min_node()
        if first_node:
            prev_node = first_node
            lists[i] = first_node.next
            min_node, i = get_min_node()
            while min_node:
                prev_node.next = min_node
                prev_node = min_node

                lists[i] = min_node.next

                min_node, i = get_min_node()
        
        return first_node