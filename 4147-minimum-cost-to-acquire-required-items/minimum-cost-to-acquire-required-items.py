
class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        common = min(need1, need2)

        ans = common * min(costBoth, cost1 + cost2)

        ans += (need1 - common) * min(cost1, costBoth)
        ans += (need2 - common) * min(cost2, costBoth)

        return ans
