class Solution(object):
    def reverse(self, x):
        
        neg = False
        if x < 0:
            x = abs(x)
            neg = True
        if neg:
            x = -int(str(x)[::-1])
        else:
            x = int(str(x)[::-1])
        
        if x.bit_length()+1 > 32:
            return 0
        
        return x
