# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m=head.next
        n=m
        while n:
            t=0
            while n.val!=0:
                t+=n.val
                n=n.next
            m.val=t
            n=n.next
            m.next=n
            m=m.next
        return head.next