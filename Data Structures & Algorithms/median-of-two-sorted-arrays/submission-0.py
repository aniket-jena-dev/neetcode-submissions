class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        total = n + m
        half = total // 2

        def helper(a, b):
            l, r = 0, len(a) - 1
            while True:
                mid = l + (r-l)//2
                parti = half - mid - 2

                aleft = a[mid] if mid >= 0 else -float('inf')
                bleft = b[parti] if parti >= 0 else -float('inf')
                aright = a[mid+1] if mid+1 < len(a) else float('inf')
                bright = b[parti+1] if parti+1 < len(b) else float('inf')

                if aleft <= bright and bleft <= aright:
                    if total % 2 == 0:
                        return (max(aleft, bleft) + min(aright, bright)) / 2
                    else:
                        return min(aright, bright)
                elif aleft > bright:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return helper(nums1, nums2) if n <= m else helper(nums2, nums1)

