class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        num = sorted(nums)
        c = 1
        mc = 1
        for i in range(1,len(num)):
            if num[i-1] == num[i]:
                continue
            if num[i-1] + 1 == num[i]:
                c += 1
            else:
                mc = max(c,mc)
                c = 1
        return max(c,mc)