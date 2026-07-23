class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0]*(max(nums)+1)
        for v in nums:
            arr[v] += 1
        print(arr)

        for i, v in enumerate(arr):
            if v > 1:
                return i
        return 0