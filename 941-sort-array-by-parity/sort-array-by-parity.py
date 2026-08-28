class Solution(object):
    def sortArrayByParity(self, nums):
        l=0
        r=len(nums)-1
        while l<r:
            if nums[l]%2!=0 and nums[r]%2==0:
                nums[l],nums[r]=nums[r],nums[l]
            if nums[l]%2==0:
                l+=1
            if nums[r]%2!=0:
                r=r-1
            
        return  nums
