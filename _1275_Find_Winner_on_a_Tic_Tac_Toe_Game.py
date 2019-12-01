from collections import defaultdict


class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        cnts = [defaultdict(int), defaultdict(int)]
        for i, (x, y) in enumerate(moves):
            cur_player = cnts[i & 1]
            cur_player['l', x] += 1
            cur_player['c', y] += 1
            if x == y: cur_player['d'] += 1
            if x + y == 2: cur_player['a'] += 1
        if max(cnts[0].values() or [0]) == 3: return 'A'
        if max(cnts[1].values() or [0]) == 3: return 'B'
        if len(moves) == 9: return 'Draw'
        return 'Pending'
