class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        # First character must be '('
        if grid[0][0] == ')':
            return False

        memo = {}

        def dfs(r, c, balance):

            # Current cell
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1

            # Too many ')'
            if balance < 0:
                return False

            # Remaining cells after this cell
            remaining = (m - 1 - r) + (n - 1 - c)

            # Not enough cells to close all '('
            if balance > remaining:
                return False

            # Reached destination
            if r == m - 1 and c == n - 1:
                return balance == 0

            # Memoization
            key = (r, c, balance)

            if key in memo:
                return memo[key]

            # Move down
            if r + 1 < m:
                if dfs(r + 1, c, balance):
                    memo[key] = True
                    return True

            # Move right
            if c + 1 < n:
                if dfs(r, c + 1, balance):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return dfs(0, 0, 0)