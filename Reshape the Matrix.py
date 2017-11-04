class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if (len(nums)*len(nums[0]))!=r*c:
            return nums
        
        flatten_matrix = []
        for a in nums:
            for b in a:
                flatten_matrix.append(b)
        final_matrix = []
        it = 0
        for a in range(0, r):
            final_matrix.append([])
            for b in range(0, c):
                final_matrix[a].append(flatten_matrix[it])
                it +=1
        return final_matrix
