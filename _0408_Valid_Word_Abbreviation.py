class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        L1, L2 = len(word), len(abbr)
        while i < L1 and j < L2:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == '0': return False
                end = L2
                for jj in xrange(j+1, L2):
                    if abbr[jj].isalpha():
                        end = jj
                        break
                num = int(abbr[j:end])
                i += num
                j += end - j
            else: return False
        if i == L1 and j == L2: return True
        return False
