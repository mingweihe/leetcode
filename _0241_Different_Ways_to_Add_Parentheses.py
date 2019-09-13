class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        for i,c in enumerate(input):
            if c in ('+', '-', '*'):
                al = self.diffWaysToCompute(input[:i])
                bl = self.diffWaysToCompute(input[i+1:])
                for x in al:
                    for y in bl:
                        if c == '+':
                            res.append(x+y)
                        elif c == '-':
                            res.append(x-y)
                        else:
                            res.append(x*y)
        if not res:
            res.append(int(input))
        return res
