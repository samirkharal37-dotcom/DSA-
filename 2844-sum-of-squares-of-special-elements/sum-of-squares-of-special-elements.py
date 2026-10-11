
class Solution(object):
    def sumOfSquares(self, nums):
        spc = 0
        n = len(nums)

        for i in range(n):
            if n % (i + 1) == 0:
                spc += nums[i] * nums[i]

        return spc
