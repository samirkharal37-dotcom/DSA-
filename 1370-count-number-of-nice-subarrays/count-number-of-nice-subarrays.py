class Solution(object):
    def numberOfSubarrays(self, nums, k):
        prefix = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            # Odd = 1, Even = 0
            prefix += num % 2

            # We need a previous prefix that is k smaller
            needed = prefix - k

            if needed in freq:
                count += freq[needed]

            # Store the current prefix sum
            freq[prefix] = freq.get(prefix, 0) + 1

        return count
        