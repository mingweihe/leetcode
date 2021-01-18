class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        ## Approach 3, kind of DP
        n = len(sentence)
        times, next_idx = [0] * n, [0] * n
        for i in xrange(n):
            idx = i
            time = 0
            j = 0
            while j + len(sentence[idx]) <= cols:
                j += len(sentence[idx]) + 1
                idx += 1
                if idx == n:
                    time += 1
                    idx = 0
            times[i] = time
            next_idx[i] = idx
            
        ans, cur_idx = 0, 0
        for _ in xrange(rows):
            ans += times[cur_idx]
            cur_idx = next_idx[cur_idx]
        return ans
            
        ## Approach 2, calculating the total length of the utilized space
        # s = ' '.join(sentence) + ' '
        # n = len(s)
        # utilized_len = 0
        # for _ in xrange(rows):
        #     utilized_len += cols
        #     if s[utilized_len % n] == ' ':
        #         utilized_len += 1
        #     else:
        #         while s[utilized_len % n - 1] != ' ':
        #             utilized_len -= 1
        # return utilized_len / n
        
        ## Approach 1, brute force + memorization, TLE
        # def get_end_pos(ccc):
        #     if ccc in cache:
        #         return cache[ccc]
        #     c = ccc
        #     r = i = 0
        #     while i < len(sentence):
        #         if c + len(sentence[i]) <= cols:
        #             c += len(sentence[i])
        #             if c == cols:
        #                 c = -1
        #                 r += 1
        #         else:
        #             c = len(sentence[i])
        #             r += 1
        #         if c + 1 < cols:
        #             c += 1
        #         else:
        #             c = 0
        #             r += 1
        #         i += 1
        #     cache[ccc] = r, c
        #     return r, c
        # cache = {}
        # i = c = res = 0
        # while i < rows:
        #     r, c = get_end_pos(c)
        #     i += r
        #     if i < rows or i == rows and c == 0:
        #         res += 1
        # return res
