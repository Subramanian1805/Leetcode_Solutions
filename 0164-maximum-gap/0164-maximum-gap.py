class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_gap = 0
        nums.sort()
        if n < 2:
            return 0
        for i in range(0,n):
            max_gap = max(max_gap,nums[i] - nums[i-1])
        return max_gap


