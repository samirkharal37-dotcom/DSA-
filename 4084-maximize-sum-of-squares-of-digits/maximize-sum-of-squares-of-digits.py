class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        nines = sum // 9
        remainder = sum % 9

        ans = "9" * nines

        if remainder > 0:
            ans += str(remainder)

        ans += "0" * (num - len(ans))

        return ans
