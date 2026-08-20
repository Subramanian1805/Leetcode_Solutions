class Solution(object):
    def pancakeSort(self, arr):
        result = []

        for size in range(len(arr), 1, -1):
            max_idx = arr.index(size)

            if max_idx != 0:
                arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
                result.append(max_idx + 1)

            if size != 1:
                arr[:size] = reversed(arr[:size])
                result.append(size)

        return result
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        