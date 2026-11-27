
class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        dp = [0] * (budget + 1)

        min_price = min(price for factor, price in items)

        for factor, price in items:
            free_items = 0

            for other_factor, _ in items:
                if other_factor % factor == 0:
                    free_items += 1

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + free_items)

        ans = 0

        for b in range(budget + 1):
            extra = (budget - b) // min_price
            ans = max(ans, dp[b] + extra)

        return ans
