class Solution(object):
    def kEmptySlots(self, bulbs, K):
        """
        :type bulbs: List[int]
        :type K: int
        :rtype: int
        [0,1,2]
        left    0   1
        right   2   3   loop stops as right reaches maximum index
        i       0   1
        """
        # Approach 2 sliding window O(n)
        days = [0] * len(bulbs)
        for i,x in enumerate(bulbs):
            days[x-1] = i
        left, right, idx = 0, K+1, 0
        res = float('inf')
        while right < len(days):
            if days[idx] < days[left] or days[idx] <= days[right]:
                if idx == right: res = min(res, max(days[left], days[right]))
                left, right = idx, idx+K+1
            idx += 1
        return -1 if res == float('inf') else res + 1

        # Approach 1 segment tree time O(n*log(n))
        # L = len(bulbs)
        # tree = [0] * 2 * L
        # def update(ind, val):
        #     ind += L
        #     tree[ind] = val
        #     while ind > 0:
        #         tree[ind>>1] = tree[ind] + tree[ind ^ 1]
        #         ind >>= 1
        # def sum_range(i, j):
        #     i += L
        #     j += L
        #     res = 0
        #     while i <= j:
        #         if i & 1:
        #             res += tree[i]
        #             i += 1
        #         if j & 1 == 0:
        #             res += tree[j]
        #             j -= 1
        #         i >>= 1
        #         j >>= 1
        #     return res
        # for i, x in enumerate(bulbs):
        #     update(x-1, 1)
        #     left, right = x-K-2, x+K
        #     if left >= 0 and tree[L+left] == 1 and sum_range(left, x-1) == 2:
        #         return i+1
        #     if right < L and tree[L+right] == 1 and sum_range(x-1, right) == 2:
        #         return i+1
        # return -1
