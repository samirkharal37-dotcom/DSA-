
class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            res = ""
            
            for i in range(0, len(s), k):
                group = s[i:i+k]
                total = sum(int(d) for d in group)
                res += str(total)
            
            s = res
        
        return s
