class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) <= 1: return 0
        A.sort()
        st = 0
        ed = len(A)-1
        if A[ed] - A[st] >= 2*K: return A[ed] - A[st] - 2*K
        elif A[ed] - A[st] <= K: return A[ed] - A[st]
        else:
            min = A[st] + k if A[st] + K < A[ed] - K else A[ed] - K
            max = A[st] + k if A[st] + K > A[ed] - K else A[ed] - K
            while st < ed:
                st += 1
                d1 = A[0] - (A[st]-K)
                d2 = (A[st]+K) - A[-1]
