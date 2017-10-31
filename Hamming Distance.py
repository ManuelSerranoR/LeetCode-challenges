class Solution(object):
    def hammingDistance(self, x, y):
        return "{0:b}".format(x^y).count("1")
