class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        myCounterP = collections.OrderedDict(sorted(collections.Counter(p).items()))
        indices = []
        for i in range(0,len(s)-(len(p)-1)):
            myCounterAux = collections.OrderedDict(sorted(collections.Counter(s[i:len(p)+i]).items()))
            if myCounterP == myCounterAux:
                indices.append(i)
        return indices
