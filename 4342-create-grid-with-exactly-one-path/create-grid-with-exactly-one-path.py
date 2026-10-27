class Solution(object):
    def createGrid(self, m, n):
        result = []

        for i in range(m):
            row = "" 

            for j in range(n):
                if i == 0 or j == n - 1:
                    row += "."
                else:
                    row += "#"

            result.append(row)  

        return result