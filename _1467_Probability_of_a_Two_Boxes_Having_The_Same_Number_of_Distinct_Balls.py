class Solution(object):
    def getProbability(self, balls):
        """
        :type balls: List[int]
        :rtype: float
        """
        def multinomial(box):
            total = sum(box)
            ans = fact[total]
            for x in box:
                ans /= fact[x]
            return ans
            
        def backtrack(idx, box1, box2):
            sum1, sum2 = sum(box1), sum(box2)
            if sum1 > max_in_one or sum2 > max_in_one : return 0
            if idx == n:
                if len(box1) == len(box2) and sum1 == sum2:
                    return multinomial(box1) * multinomial(box2)
                else: return 0
            ans = 0
            for i in xrange(balls[idx] + 1):
                b1, b2 = i, balls[idx] - i
                if b1: box1 += b1,
                if b2: box2 += b2,
                ans += backtrack(idx+1, box1, box2)
                if b1: box1.pop()
                if b2: box2.pop()
            return ans
        
        fact = [1]
        for i in xrange(1, 49):
            fact += fact[-1] * i,
            
        n = len(balls)
        max_in_one = sum(balls) / 2
        num_total = multinomial(balls)
        num_valids = backtrack(0, [], [])
        return float(num_valids) / num_total
