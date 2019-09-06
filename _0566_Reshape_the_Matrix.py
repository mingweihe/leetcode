import numpy as np


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # Approach 3
        try: return np.array(nums).reshape([r,c]).tolist()
        except Exception: return nums

        # Approach 2
        # flat = sum(nums, [])
        # if len(flat) != r * c: return nums
        # tuples = zip(*([iter(flat)] * c))
        # return map(list, tuples)

        # Approach 1
        # if not nums[0]: return nums
        # LR, LC = len(nums), len(nums[0])
        # if LR * LC != r * c: return nums
        # res, cnt, curR = [], 0, [0] * c
        # for i in range(LR):
        #     for j in range(LC):
        #         curR[cnt] = nums[i][j]
        #         cnt += 1
        #         if cnt == c:
        #             cnt = 0
        #             res.append(curR)
        #             curR = [0] * c
        # return res
