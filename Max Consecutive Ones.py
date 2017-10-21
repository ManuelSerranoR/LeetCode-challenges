class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summation = 0
        maxi = 0
        for n in nums:
            if n==0:
                summation = 0
            else:
                summation+=1
                maxi = max(maxi, summation)
        return maxi
