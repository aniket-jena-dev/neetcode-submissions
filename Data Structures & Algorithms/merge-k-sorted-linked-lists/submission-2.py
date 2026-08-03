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
        while len(lists) > 1:
            arr = []
            for i in range(0, len(lists), 2):
                l1, l2 = lists[i], lists[i+1] if i+1 < len(lists) else None
                arr.append(self.merge2Lists(l1, l2))
            lists = arr
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
        
