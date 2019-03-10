class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        num = [ 0, 0]
        same = 0
        for flag_idx in range(2): # [ A[0], B[0]]:
            flag = [ A[0], B[0]][flag_idx]
            for idx in range(1, len(A)):
                same += int(A[idx] == B[idx])
                if flag == A[idx]:
                    if A[idx] != B[idx]:
                        num[flag_idx] += int(flag_idx == 1)
                elif flag == B[idx]:
                    if A[idx] != B[idx]:
                        num[flag_idx] += int(flag_idx == 0)
                else:
                    num[flag_idx] = -1
                    break

        if num[0] < 0 and num[1]<0: return -1
        elif num[0] < 0: return min(num[1], len(A)-num[1]-same)
        elif num[1] < 0: return min(num[0], len(A)-num[0]-same)
        else: return min(num[1], max(len(A)-num[1], 0), num[0], max(len(A)-num[0], 0) )
