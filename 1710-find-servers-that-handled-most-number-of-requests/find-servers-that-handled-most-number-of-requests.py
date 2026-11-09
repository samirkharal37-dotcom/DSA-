
import heapq
from sortedcontainers import SortedList

class Solution(object):
    def busiestServers(self, k, arrival, load):
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, s = heapq.heappop(busy)
                available.add(s)

            if not available:
                continue

            j = available.bisect_left(i % k)

            if j == len(available):
                j = 0

            s = available.pop(j)
            count[s] += 1
            heapq.heappush(busy, (a + l, s))

        mx = max(count)
        return [i for i in range(k) if count[i] == mx]
