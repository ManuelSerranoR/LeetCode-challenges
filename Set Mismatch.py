class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count_occurances = [0]*(len(nums))
        for n in nums:
            count_occurances[n-1]+=1
        repeated = count_occurances.index(2)+1
        missing = count_occurances.index(0)+1
        return repeated, missing
