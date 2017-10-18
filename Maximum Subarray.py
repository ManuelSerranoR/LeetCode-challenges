class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        def findCross(nums):
        
            mid = int((len(nums)+1)/2)

            sum_left = -1000
            sum_aux = 0
            for n in reversed(nums[:mid]):
                sum_aux+=n
                if sum_aux>sum_left:
                    sum_left = sum_aux

            sum_right = -1000
            sum_aux = 0
            for n in nums[mid:]:
                sum_aux+=n
                if sum_aux>sum_right:
                    sum_right = sum_aux
            return sum_left + sum_right
        
        
        max_cross = findCross(nums)
        if len(nums)==1:
            return int(nums[0])
        else:
            mid = int((len(nums)+1)/2)
            max_left = self.maxSubArray(nums[:mid])
            max_right = self.maxSubArray(nums[mid:])
            print (max_left,max_right,max_cross)
            return max(max_left,max_right,max_cross)
