class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        myString = ""
        s_list = s.split(" ")
        for i, n in enumerate(s_list):
            myString += n[::-1]
            if i != len(s_list)-1:
                myString += " "
        return myString
