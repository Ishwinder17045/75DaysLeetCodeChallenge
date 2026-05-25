class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        max_freq = max(freq.values())

        count_max = 0

        for val in freq.values():
            if val == max_freq:
                count_max += 1

        intervals = (max_freq - 1) * (n + 1) + count_max

        return max(len(tasks), intervals)