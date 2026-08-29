class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        prefix_count = {0: 1}

        for num in nums:
            prefix_sum += num

            needed = prefix_sum - k

            if needed in prefix_count:
                count += prefix_count[needed]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        return count