class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) <= 1: return 0
        A.sort()
        diff = A[-1] - A[0]
        if diff > 2*K: return diff-2*K
        else: return 0
