class Solution(object):
    def sumOfUnique(self, nums):
        freq={}
        total=0
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in freq:
            if freq[num]==1:
                total+=num
        return total