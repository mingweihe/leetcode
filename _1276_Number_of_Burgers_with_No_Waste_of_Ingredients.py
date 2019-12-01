class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        Math problem
        say, res = [x, y]
        then, 4x+2y = tomatoSlices,
              x+y = cheeseSlices
        make sure x, y be integers and greater or equal than 0
        """
        y = 2 * cheeseSlices - tomatoSlices / 2.
        x = cheeseSlices - y
        if x < 0 or y < 0 or y != int(y) or x != int(x): return []
        return [int(x), int(y)]
