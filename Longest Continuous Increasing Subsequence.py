class Solution(object):
    def findLengthOfLCIS(self, nums):
        if nums==[]: return 0
        maxi = 1
        maxi_temp = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                maxi_temp+=1
                maxi = max(maxi, maxi_temp)
            else: 
                maxi_temp = 1
        return maxi
