import collections


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # Approach 3
        base = collections.Counter('balloon')
        cnt = collections.Counter(text)
        return min([cnt[c] / base[c] for c in base])

        # Approach 2
        # A = [0]*26
        # for c in text: A[ord(c)-97] += 1
        # res = A[ord('b')-97]
        # res = min(res, A[ord('b')-97])
        # res = min(res, A[ord('a')-97])
        # res = min(res, A[ord('l')-97]/2)
        # res = min(res, A[ord('o')-97]/2)
        # res = min(res, A[ord('n')-97])
        # return res

        # Approach 1
        # d = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        # for c in text:
        #     if c in ['b', 'a', 'n']:
        #         d[c] += 1
        #     elif c in ['l', 'o']:
        #         d[c] += .5
        # return int(min(d.values() or [0]))
