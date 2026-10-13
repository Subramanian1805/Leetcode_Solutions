class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return True if len(nums) != len(set(nums)) else False 