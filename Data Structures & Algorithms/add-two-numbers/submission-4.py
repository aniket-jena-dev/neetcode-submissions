# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        h = dummy
        carry = 0
        while l1 and l2:
            curr_sum = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            h.next = ListNode(curr_sum)
            h = h.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            curr_sum = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            h.next = ListNode(curr_sum)
            h = h.next
            l1 = l1.next
        while l2:
            curr_sum = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            h.next = ListNode(curr_sum)
            h = h.next
            l2 = l2.next
        if carry > 0:
            h.next = ListNode(carry)
        return dummy.next