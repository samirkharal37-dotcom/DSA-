class Solution(object):
    def getWinner(self, arr, k):
        winner = arr[0]
        streak = 0

        for i in range(1, len(arr)):
            if winner > arr[i]:
                streak += 1
            else:
                winner = arr[i]
                streak = 1

            if streak == k:
                return winner

        return winner