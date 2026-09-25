class Solution(object):
    def longestPalindrome(self, s):

        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expand(s, i, i)     # odd length
            len2 = self.expand(s, i, i + 1) # even length
            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
