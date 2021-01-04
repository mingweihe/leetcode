class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: -x[1])
        res = 0
        i = 0
        while i < len(boxTypes) and truckSize > 0:
            numberOfBoxes, numberOfUnitsPerBox = boxTypes[i]
            curNum = min(truckSize, numberOfBoxes)
            truckSize -= curNum
            res += curNum * numberOfUnitsPerBox
            i += 1
        return res
