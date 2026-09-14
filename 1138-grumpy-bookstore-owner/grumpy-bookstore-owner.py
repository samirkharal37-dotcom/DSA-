class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):

        satisfied = 0

        window = 0
        max_window = 0

        for i in range(len(customers)):

            if grumpy[i] == 0:
                satisfied += customers[i]

            else:
                window += customers[i]

            if i >= minutes and grumpy[i - minutes] == 1:
                window -= customers[i - minutes]

            max_window = max(max_window, window)

        return satisfied + max_window