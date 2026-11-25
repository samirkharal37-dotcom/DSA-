
class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        # Step 1: Build Suffix Array
        sa = list(range(n))
        rank = nums[:]
        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            new_rank = [0] * n

            for j in range(1, n):
                a, b = sa[j - 1], sa[j]

                prev = (rank[a],
                        rank[a + k] if a + k < n else -1)

                curr = (rank[b],
                        rank[b + k] if b + k < n else -1)

                new_rank[b] = new_rank[a] + (prev != curr)

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        # Step 2: Build inverse suffix array
        pos = [0] * n

        for i in range(n):
            pos[sa[i]] = i

        # Step 3: Build LCP Array (Kasai's algorithm)
        lcp = [0] * n
        h = 0

        for i in range(n):
            r = pos[i]

            if r == 0:
                h = 0
                continue

            j = sa[r - 1]

            while i + h < n and j + h < n:
                if nums[i + h] != nums[j + h]:
                    break
                h += 1

            lcp[r] = h

            if h > 0:
                h -= 1

        # Step 4: Find minimum unique subarray
        ans = n

        for i in range(n):
            r = pos[i]

            left = lcp[r]
            right = lcp[r + 1] if r + 1 < n else 0

            length = max(left, right) + 1

            # Subarray must fit inside nums
            if length <= n - i:
                ans = min(ans, length)

        return ans
