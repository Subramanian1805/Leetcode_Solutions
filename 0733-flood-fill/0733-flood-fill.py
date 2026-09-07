from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]

        if old == color:
            return image

        rows, cols = len(image), len(image[0])
        q = deque([(sr, sc)])
        image[sr][sc] = color

        while q:
            r, c = q.popleft()

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    image[nr][nc] == old):

                    image[nr][nc] = color
                    q.append((nr, nc))

        return image