class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()

        def can_place(distance: int) -> bool:
            balls = 1
            last_position = position[0]

            for pos in position[1:]:
                if pos - last_position >= distance:
                    balls += 1
                    last_position = pos

                    if balls == m:
                        return True

            return False

        left = 1
        right = position[-1] - position[0]

        while left <= right:
            mid = (left + right) // 2

            if can_place(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right