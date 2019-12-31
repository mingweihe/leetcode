class Solution(object):
    def isSolvable(self, words, result):
        """
        :type words: List[str]
        :type result: str
        :rtype: bool
            Time complexity O(n!)
        """
        def search(idx, pos, carry):
            if idx == max_word_len:
                if carry == 0: return True
                return False
            if pos == len(words):
                for i in xrange(pos-1):
                    if idx < len(words[i]): carry += reps[ord(words[i][idx])-65]
                carry, pos_sum = divmod(carry, 10)
                if idx >= len(result) or reps[ord(result[idx]) - 65] != pos_sum:
                    return False
                return search(idx+1, 0, carry)
            if idx >= len(words[pos]): return search(idx, pos+1, carry)
            k = ord(words[pos][idx]) - 65
            if reps[k] != -1: return search(idx, pos+1, carry)
            if reps[k] == 0 and idx == len(words[pos]) - 1: return False
            for i in xrange(10):
                if used[i]: continue
                reps[k] = i
                used[i] = True
                if search(idx, pos+1, carry): return True
                reps[k] = -1
                used[i] = False
            return False
        result = result[::-1]
        words = [w[::-1] for w in words] + [result]
        max_word_len = max(map(len, words))
        reps = [-1] * 26
        used = [False] * 10
        return search(0, 0, 0)
