from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Approach 2
        max_len = max(map(lambda x: len(str(x)), nums))
        return str(int(''.join(sorted(map(str, nums), key=lambda x: x*(max_len/len(x)+1), reverse=True))))

        # Approach 1
        # return str(int(''.join(sorted(map(str, nums), \
        #     cmp=lambda x,y: 2*int(x+y<y+x)-1))))
        # python3
        # return str(int(''.join(sorted(map(str, nums), key=cmp_to_key(lambda x, y: 2 * int(x + y < y + x) - 1)))))
