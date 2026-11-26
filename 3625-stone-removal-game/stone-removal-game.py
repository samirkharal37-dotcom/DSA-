
class Solution(object):
    def canAliceWin(self, n):
        stones = n
        remove = 10
        alice = True

        while stones >= remove:
            stones -= remove
            remove -= 1
            alice = not alice

        return not alice
