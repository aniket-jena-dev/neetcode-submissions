# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
      
        if n < 2:
            if lists:
                return lists[0]
            else:
                return
        for i in range(1, n):
            lists[0] = self.merge2Lists(lists[0], lists[i])
        return lists[0]

    def merge2Lists(self, l1, l2):
        h1 = l1
        h2 = l2
        dummy = ListNode()
        dummyH = dummy

        while h1 and h2:
            if h1.val <= h2.val:
                dummyH.next = h1
                h1 = h1.next
            else:
                dummyH.next = h2
                h2 = h2.next
            dummyH = dummyH.next

        while h1:
            dummyH.next = h1
            h1 = h1.next
            dummyH = dummyH.next
        
        while h2:
            dummyH.next = h2
            h2 = h2.next
            dummyH = dummyH.next
        
        return dummy.next
        
