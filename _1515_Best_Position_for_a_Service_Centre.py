class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
            Simulated annealing algorithm
        """
        def dist(Xc, Yc):
            return sum(map(lambda (x, y): math.sqrt((Xc-x)**2+(Yc-y)**2), positions))
        c_x, c_y = 50, 50
        res = dist(50, 50)
        step = 1.0
        while step >= 0.000001:
            decrease = True
            for dx, dy in [[0, step], [0, -step], [step, 0], [-step, 0]]:
                cur_x, cur_y = c_x+dx, c_y+dy
                cur_dist = dist(cur_x, cur_y)
                if cur_dist < res:
                    decrease = False
                    res = cur_dist
                    c_x, c_y = cur_x, cur_y
            if decrease:
                step /= 10
        return res
