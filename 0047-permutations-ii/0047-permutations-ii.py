class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        path = []
        used = [False] * len(nums)

        nums.sort()

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack()

                path.pop()
                used[i] = False

        backtrack()

        return result
