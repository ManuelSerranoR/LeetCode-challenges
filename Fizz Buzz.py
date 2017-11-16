class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        myList = []
        for i in range(1, n+1):
            if not i%3:
                if not i%5:
                    myList.append("FizzBuzz")
                    continue
                myList.append("Fizz")
                continue
            if not i%5:
                myList.append("Buzz")
                continue
            myList.append(str(i))
        return myList
        
