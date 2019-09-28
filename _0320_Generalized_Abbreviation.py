class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
            time O(2^n) space O(n) -> function stack
        """
        def helper(ans, cur, pos, cnt):
            if pos == len(word):
                if cnt != 0: cur += str(cnt)
                ans.append(cur)
                return
            helper(ans, cur, pos+1, cnt+1)
            num = str(cnt) if cnt != 0 else ''
            helper(ans, cur + num + word[pos], pos+1, 0)
        res = []
        helper(res, '', 0, 0)
        return res
