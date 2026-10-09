class Solution(object):
    def minInsertions(self, s):
        openn = 0
        ans = 0

        i = 0
        while i < len(s):
            if s[i] == "(":
                openn += 1

                if openn > 0:
                    pass

                i += 1

            else:
                if i + 1 < len(s) and s[i + 1] == ")":
                    i += 2
                else:
                    ans += 1
                    i += 1

                if openn > 0:
                    openn -= 1
                else:
                    ans += 1

        return ans + 2 * openn