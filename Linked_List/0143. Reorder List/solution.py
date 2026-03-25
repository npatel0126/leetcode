# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        
        slow = fast = head

        #Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow

        #Reverse second half of list
        while curr: 
            curr.next, prev, curr = prev, curr, curr.next

        first = head 
        second = prev

        #Merge the lists together 
        while second.next:
            first.next, second.next, first, second = second, first.next, first.next, second.next

        
