class Solution(object):
    def maximumSaleItems(self, items, budget):
        items.sort(key=lambda x: x[1])

        n = len(items)
        max_factor = max(item[0] for item in items)

        # Count frequency of each factor
        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count items whose factors are multiples
        for i in range(1, max_factor + 1):
            for j in range(i * 2, max_factor + 1, i):
                freq[i] += freq[j]

        min_price = items[0][1]
        ans = 0

        # Buy items that provide an additional free item
        for factor, price in items:
            if price > 2 * min_price:
                break

            free_count = freq[factor] - 1

            take = min(free_count, budget // price)

            ans += take * 2
            budget -= take * price

        # Use remaining budget to buy cheapest items
        ans += budget // min_price

        return ans