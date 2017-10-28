class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        isHappy = None
        def happy(n):
            number = 0
            for i in str(n):
                number += int(i)**2
            return number
        i = 0
        while happy(n) != 1:
            n = happy(n)
            i+=1
            if i == 7:
                return False
        
        return True
