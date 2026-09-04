from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        # (time, node)
        heap = [(0, k)]
        dist = {}

        while heap:
            time, node = heappop(heap)

            if node in dist:
                continue

            dist[node] = time

            for nei, weight in graph[node]:
                if nei not in dist:
                    heappush(heap, (time + weight, nei))

        return max(dist.values()) if len(dist) == n else -1