
class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Build the original tree
        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        ans = [1] * n
        prev = [-1] * n
        last = {}

        # Iterative DFS
        stack = [0]

        while stack:
            node = stack.pop()

            if node >= 0:
                # Find nearest ancestor with same character
                prev[node] = last.get(s[node], -1)

                last[s[node]] = node

                # Exit marker
                stack.append(~node)

                # Visit children
                stack.extend(tree[node])

            else:
                node = ~node

                # Restore previous ancestor of this character
                last[s[node]] = prev[node]

                # Determine final parent
                p = prev[node]

                if p == -1:
                    p = parent[node]

                # Add subtree size to final parent
                if p != -1:
                    ans[p] += ans[node]

        return ans
