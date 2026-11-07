class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n=len(servers)
        m=len(tasks)
        ans=[0]*m
        available=[(servers[i],i) for i in range(n)]
        heapq.heapify(available)
        busy=[]
        for i in range(m):
            while busy and busy[0][0]<=i:
                freetime,server=heapq.heappop(busy)
                heapq.heappush(available,server)
            if available:
                weight,idx=heapq.heappop(available)
                ans[i]=idx
                heapq.heappush(busy,(i+tasks[i],(weight,idx)))
            else:
                freetime,server=heapq.heappop(busy)
                weight,idx=server
                ans[i]=idx
                heapq.heappush(busy,(freetime+tasks[i],server))
        return ans