class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            if task in count:
                count[task] += 1
            else:
                count[task] = 1

        max_count = max(count.values())

        max_tasks = 0

        for value in count.values():
            if value == max_count:
                max_tasks += 1

        part = (max_count - 1) * (n + 1) + max_tasks

        answer = max(len(tasks), part)

        return answer