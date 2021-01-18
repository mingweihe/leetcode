class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def is_strachy(word):
            i, j = 0, 0
            m, n = len(S), len(word)
            while i < m and j < n:
                if S[i] != word[j]: return False
                start_i, start_j = i, j
                while i < m and S[i] == S[start_i]: i += 1
                while j < n and word[j] == word[start_j]: j += 1
                len_g_s = i - start_i
                len_g_w = j - start_j
                if len_g_s < len_g_w: return False
                elif len_g_s == len_g_w: continue
                if len_g_s == 2: return False
            return i == m and j == n
        
        return len(filter(is_strachy, words))
