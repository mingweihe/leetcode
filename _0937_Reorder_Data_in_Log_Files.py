class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # Approach 3
        def keys(log):
            id_, rest = log.split(' ', 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)
        return sorted(logs, key=keys)

        # Approach 2
        # letterLogs = filter(lambda x: x[x.find(' ')+1].isalpha(), logs)
        # digitLogs = filter(lambda x: x[x.find(' ')+1].isdigit(), logs)
        # letterLogs.sort(key=lambda x: (x[x.find(' '):], x[:x.find(' ')]))
        # return letterLogs + digitLogs

        # Approach 1
        # res_letters = []
        # res_digits = []
        # for x in logs:
        #     first = x[x.find(' ')+1]
        #     if first.isdigit(): res_digits.append(x)
        #     else: res_letters.append(x)
        # res_letters.sort(key=lambda x: (x[x.find(' '):], x[:x.find(' ')]))
        # return res_letters + res_digits
