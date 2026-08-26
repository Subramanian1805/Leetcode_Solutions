class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        n = len(nums)
        left = (n - 1) // 2
        right = n - 1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = arr[left]
                left -= 1
            else:
                nums[i] = arr[right]
                right -= 1