class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        myOddMax = 0
        if s == '':
            return 0
        myCounter = collections.Counter(s) #key->character, value->count
        #get highest odd count
        aux = [i for i in myCounter.values() if i%2]
        if aux!=[]:
            myOddMax = max(aux)
            aux.remove(myOddMax)
        b=0
        
        for n in aux:
            if n>1: 
                b+=n-1
                
        return myOddMax + sum(i for i in myCounter.values() if not i%2)+b
