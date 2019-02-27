class Solution:
    '''
    Desc:我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
          - B.length >= 3
          - 存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
         （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
         给出一个整数数组 A，返回最长 “山脉” 的长度。
         如果不含有 “山脉” 则返回 0。
    Link: https://leetcode-cn.com/problems/longest-mountain-in-array/
    Solution: 模拟，注意边界条件
    '''
    def longestMountain(self, A: List[int]) -> int:
        res = 0
        if len(A) < 3: return res
        else:
            st = 0
            val = A[st]
            p = 0 # phase: 0, raise; 1, fall
            for idx2 in range(st+1, len(A)):
                if p == 0: # raise phase
                    if A[idx2] < val:
                        if idx2-st == 1:
                            st = idx2
                            val = A[st]
                        else:
                            res = idx2 - st + 1 if idx2 - st + 1 > res else res
                            top = idx2 - 1
                            val = A[idx2]
                            p = 1
                    elif A[idx2] == val:
                        st = idx2
                        val = A[st]
                    else:
                        val = A[idx2]
                else: # fall phase
                    if A[idx2] < val:
                        val = A[idx2]
                        res = idx2 - st + 1 if idx2 - st + 1 > res else res
                    else:
                        res = (idx2 - st) if (idx2 - st) > res else res
                        if A[idx2] > val:
                            st = idx2 - 1
                        else:
                            st = idx2
                        val = A[idx2]
                        p = 0

        return res
