
class Solution:
    def palindromePath(self, n, edges, s, queries):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        L = n.bit_length()
        par = [[0] * n for _ in range(L)]
        tin, tout, dep = [0]*n, [0]*n, [0]*n
        pre = [0]*n
        t = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()
            if state:
                tout[u] = t
                continue
            par[0][u] = u if p < 0 else p
            pre[u] = (pre[p] if p >= 0 else 0) ^ (1 << (ord(s[u])-97))
            tin[u] = t
            t += 1
            stack.append((u, p, 1))
            for v in g[u]:
                if v != p:
                    dep[v] = dep[u] + 1
                    stack.append((v, u, 0))

        for k in range(1, L):
            for u in range(n):
                par[k][u] = par[k-1][par[k-1][u]]

        def lca(u, v):
            if dep[u] < dep[v]:
                u, v = v, u
            d = dep[u] - dep[v]
            for k in range(L):
                if d >> k & 1:
                    u = par[k][u]
            if u == v:
                return u
            for k in range(L-1, -1, -1):
                if par[k][u] != par[k][v]:
                    u, v = par[k][u], par[k][v]
            return par[0][u]

        bit = [0] * (n + 2)

        def add(i, x):
            i += 1
            while i <= n + 1:
                bit[i] ^= x
                i += i & -i

        def update(u, x):
            add(tin[u], x)
            add(tout[u], x)

        def get(u):
            x, i = 0, tin[u] + 1
            while i:
                x ^= bit[i]
                i -= i & -i
            return pre[u] ^ x

        ans, s = [], list(s)
        for q in queries:
            a = q.split()
            u = int(a[1])
            if a[0] == "update":
                x = 1 << (ord(s[u])-97)
                y = 1 << (ord(a[2])-97)
                update(u, x ^ y)
                s[u] = a[2]
            else:
                v = int(a[2])
                w = lca(u, v)
                x = get(u) ^ get(v) ^ (1 << (ord(s[w])-97))
                ans.append(x & (x-1) == 0)

        return ans
