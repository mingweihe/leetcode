class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        index = 0
        res = []
        L = len(words)
        while index < L:
            last = index + 1
            count = len(words[index])
            while last < L:
                if count + 1 + len(words[last]) > maxWidth: break
                count += 1 + len(words[last])
                last += 1
            cur = words[index]
            diff = last - index - 1
            if last == L or diff == 0:
                for i in xrange(index+1, last):
                    cur += ' ' + words[i]
                cur += ' ' * (maxWidth-count)
            else:
                spaces = (maxWidth - count) / diff + 1
                extras = (maxWidth - count) % diff
                for i in xrange(index+1, last):
                    cur += ' ' * spaces
                    if extras:
                        cur += ' '
                        extras -= 1
                    cur += words[i]
            res.append(cur)
            index = last
        return res
