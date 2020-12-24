from functools import lru_cache
from collections import defaultdict


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        ## Approach 2
        @lru_cache(None)
        def dfs(i, k):
            if len(s) - i <= k: return 0
            res = float('inf')
            cnt = defaultdict(int)
            most_freq = 0
            for j in range(i, len(s)):
                cnt[s[j]] += 1
                most_freq = max(most_freq, cnt[s[j]])
                non_most_freq = j-i+1-most_freq
                if non_most_freq > k: break
                compressed_len = 1 if most_freq == 1 else len(str(most_freq)) + 1
                res = min(res, compressed_len + dfs(j+1, k-non_most_freq))
            return res
        return dfs(0, k)
        
        ## Approach 1
        # @lru_cache(None)
        # def dfs(i, last, last_count, k):
        #     if k < 0: return float('inf')
        #     if i == len(s): return 0
        #     if s[i] == last:
        #         carry = 1 if last_count in (1, 9, 99) else 0
        #         return carry + dfs(i+1, last, last_count + 1, k)
        #     else:
        #         res_del = dfs(i+1, last, last_count, k-1)
        #         res_keep = 1 + dfs(i+1, s[i], 1, k)
        #         return min(res_del, res_keep)
        # return dfs(0, '', 0, k)
