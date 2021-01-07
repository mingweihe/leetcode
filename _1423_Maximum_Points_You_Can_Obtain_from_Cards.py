from itertools import accumulate


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        accums = [0] + list(accumulate(cardPoints))
        res = 0
        for i in range(k+1):
            left = accums[i]
            right = accums[-1] - accums[len(accums)-1-k+i]
            res = max(res, left + right)
        return res
