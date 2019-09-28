import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach 2 stack
        cnt = collections.Counter(s)
        stack, seen = [], set()
        for c in s:
            cnt[c] -= 1
            if c in seen: continue
            while stack and cnt[stack[-1]] != 0 and stack[-1] > c:
                seen.discard(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack)

        # Approach 1 hash map
        # res = ''
        # dic = {s[i]: i for i in xrange(len(s))}
        # start, end = 0, min(dic.values() or [0])
        # for i in xrange(len(dic)):
        #     min_letter = '{' # chr(ord('z') + 1)
        #     for j in xrange(start, end+1):
        #         if s[j] in dic and s[j] < min_letter:
        #             min_letter = s[j]
        #             start = j + 1
        #     res += min_letter
        #     del dic[min_letter]
        #     if s[end] == min_letter:
        #         end = min(dic.values() or [0])
        # return res
