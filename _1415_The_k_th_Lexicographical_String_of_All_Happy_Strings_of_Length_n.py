from collections import deque


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ## Approach 3, bfs
        dq = deque(['a', 'b', 'c'])
        next_chars = {'a': 'bc', 'b': 'ac', 'c': 'ab'}
        while len(dq[0]) != n:
            u = dq.popleft()
            for v in next_chars[u[-1]]:
                dq.append(u+v)
        return dq[k-1] if len(dq) >= k else ''
            
        ## Approach 2, dfs using yield, yield from
#         def generate(prev):
#             if len(prev) == n:
#                 yield prev
#                 return
#             for c in 'abc':
#                 if not prev or c != prev[-1]:
#                     yield from generate(prev+c)
                    
#         for i, x in enumerate(generate(''), 1):
#             if i == k:
#                 return x
#         return ''
                
        ## Approach 1
        # def happy(A):
        #     for i in range(len(A)-1):
        #         if A[i] == A[i+1]: return False
        #     return True
        # A = sorted([x for x in product(['a', 'b', 'c'], repeat=n) if happy(x)])
        # return '' if k > len(A) else ''.join(A[k-1])
