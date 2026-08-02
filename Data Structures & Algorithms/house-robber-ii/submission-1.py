class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[-1]
        return max(self.robH(nums[1:n]), self.robH(nums[0:n-1]))

    def robH(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[-1]
        dp = [0]*n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]
        