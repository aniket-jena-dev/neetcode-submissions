# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            tail = curr
            counter = 0
            while curr and counter < k:
                curr = curr.next
                counter += 1

            if counter < k:
                prev.next = tail
            else:
                prev.next = self.rev(tail, k)
                prev = tail

        return dummy.next

    def rev(self, tail, k):
        prev = None
        curr = tail
        while tail and k > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k -= 1
        return prev
