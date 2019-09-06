class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # Approach 3
        res = []
        for i in range(12):
            num1ini = bin(i).count('1')
            for j in range(60):
                if num1ini + bin(j).count('1') == num:
                    res.append(str(i)+':'+'{:02}'.format(j))
        return res

        # Approach 2
        # res = []
        # for i in range(60):
        #     num1ini = (1&i)+(0!=(2&i))+(0!=(4&i))+(0!=(8&i))+(0!=(16&i))+(0!=(32&i))
        #     for j in range(12):
        #         if num1ini+(1&j)+(0!=(2&j))+(0!=(4&j))+(0!=(8&j)) == num:
        #             res.append('%d:%02d'%(j,i))
        # return res
        
        # Approach 1
        # return ['%d:%02d'%(h,m) for h in range(12) for m in range(60) if (bin(h)+bin(m)).count('1') == num]
