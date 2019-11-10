class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        row1 = []
        row2 = []
        for i, x in enumerate(colsum):
            num1, num2 = 0, 0
            if upper > 0 or lower > 0:
                if colsum[i] == 2:
                    upper -= 1
                    lower -= 1
                    num1 = num2 = 1
                elif colsum[i] == 1:
                    if upper > lower:
                        upper -= 1
                        num1 = 1
                    else:
                        lower -= 1
                        num2 = 1
            else:
                if colsum[i] != 0: return []
            row1 += num1,
            row2 += num2,
        return [] if upper != 0 or lower != 0 else [row1,row2]
