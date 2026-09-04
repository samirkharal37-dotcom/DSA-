class Solution(object):
    def xorOperation(self, n, start):
        nums=[]
        res=0
        for i in range(n):
            nums=start+2*i
            res=res^nums
        return res  