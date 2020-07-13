class Solution(object):
    def __init__(self):
        self.note = dict()
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        if not self.note.get(N):
            res = self.fib(N-1)+self.fib(N-2)
            self.note[N] = res
        return self.note[N]
