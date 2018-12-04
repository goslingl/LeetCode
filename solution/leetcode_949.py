class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort()
        B = A[:]
        max_list = [2, 3, 5, 9]
        time = ""
        for idx in range(len(A)):
            res, res_idx = self.get_max(B, max_list[idx])
            if res < 0: return ""
            del B[res_idx]
            time = time + str(res)
            if idx == 0 and res <= 1: max_list[1] = 9
            if idx == 1: time = time + ":"
        return time

    def get_max(self, A, max):
        for idx in range(len(A)-1, -1, -1):
            if A[idx] <= max:
                if len(A) == 4 and A[0] <= 1 and A[1] == 2 and A[2] > 5: return A[0],0
                return A[idx], idx
        return -1,-1

if __name__ == '__main__':
    s = Solution()
    A = [1,2,3,4]
    print(A, s.largestTimeFromDigits(A))
    A = [2,2,3,4]
    print(A, s.largestTimeFromDigits(A))
    A = [6,2,3,4]
    print(A, s.largestTimeFromDigits(A))
    A = [6,7,3,4]
    print(A, s.largestTimeFromDigits(A))
    A = [0,7,3,4]
    print(A, s.largestTimeFromDigits(A))
    A = [0,1,0,0]
    print(A, s.largestTimeFromDigits(A))
    A = [0,4,0,0]
    print(A, s.largestTimeFromDigits(A))
    A = [1,4,0,0]
    print(A, s.largestTimeFromDigits(A))
    A = [0,6,6,2]
    print(A, s.largestTimeFromDigits(A))
    A = [0,6,9,1]
    print(A, s.largestTimeFromDigits(A))
    A = [2,8,9,1]
    print(A, s.largestTimeFromDigits(A))
