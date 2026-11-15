
class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7

        odd = 0
        even = 1
        prefix = 0
        res = 0

        for num in arr:
            prefix += num

            if prefix % 2 == 0:
                res += odd
                even += 1
            else:
                res += even
                odd += 1

        return res % MOD
