
from bisect import bisect_left

class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)

        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def add(bit, i, v):
            while i <= m:
                bit[i] += v
                i += i & -i

        def query(bit, i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        def kth(k):
            i = 0
            step = 1 << (m.bit_length() - 1)
            while step:
                j = i + step
                if j <= m and cnt[j] < k:
                    i = j
                    k -= cnt[j]
                step >>= 1
            return i + 1

        costs = []
        total = 0

        for i, v in enumerate(nums):
            p = bisect_left(vals, v) + 1
            add(cnt, p, 1)
            add(sm, p, v)
            total += v

            if i >= x:
                v = nums[i - x]
                p = bisect_left(vals, v) + 1
                add(cnt, p, -1)
                add(sm, p, -v)
                total -= v

            if i >= x - 1:
                p = kth((x + 1) // 2)
                med = vals[p - 1]

                c = query(cnt, p)
                s = query(sm, p)

                costs.append(med * c - s + total - s - med * (x - c))

        inf = float('inf')
        dp = [0] * (n + 1)

        for j in range(1, k + 1):
            ndp = [inf] * (n + 1)

            for i in range(1, n + 1):
                ndp[i] = ndp[i - 1]

                if i >= x:
                    ndp[i] = min(
                        ndp[i],
                        dp[i - x] + costs[i - x]
                    )

            dp = ndp

        return dp[n]
