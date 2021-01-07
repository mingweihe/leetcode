class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dp = {0: -1}
        res = n = len(nums)
        need = sum(nums) % p
        if need == 0: return 0
        cur = 0
        for i, x in enumerate(nums):
            cur = (cur + x) % p
            if (cur-need) % p in dp:
                res = min(res, i - dp[(cur-need) % p])
            dp[cur] = i
        return -1 if res == n else res
