class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # Approach 2
        s, c, j = '', 1, 0
        for i in chars:
            if i != s:
                if c > 1:
                    for k in str(c):
                        chars[j] = k
                        j += 1
                chars[j] = i
                j += 1
                s, c = i, 1
            else: c += 1
        if c > 1:
            for k in str(c):
                chars[j] = k
                j += 1
        return j

        # Approach 1
        # left = i = 0
        # while i < len(chars):
        #     chars[left], length = chars[i], 1
        #     while (i + 1) < len(chars) and chars[i] == chars[i + 1]:
        #         i, length = i + 1, length + 1
        #     if length > 1:
        #         _length = str(length)
        #         chars[left + 1:left + 1 + len(_length)] = _length
        #         left += len(_length)
        #     i, left = i + 1, left + 1
        # return left
