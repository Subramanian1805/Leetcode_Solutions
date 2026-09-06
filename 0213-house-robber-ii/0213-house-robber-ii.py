class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev2 = prev1 = 0

            for money in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + money)

            return prev1

        # Since the first and last houses are adjacent:
        # 1. Exclude the last house
        # 2. Exclude the first house
        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )