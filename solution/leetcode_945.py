# pass

class Solution:
    def minIncrementForUnique(self, A):
        res = 0
        if len(A) <= 1:  return res
        A.sort()
        cur, num = -1, 0
        for root in A:
            if cur < 0: 
                cur, num = root, 1
            else:
                if root == cur:
                    num += 1
                else:
                    if num > (root - cur):
                        res += (root - cur) * (num - 1) - (root - cur) * (root - cur -1) / 2
                        #print('add:', (root - cur) * (num - 1) - (root - cur) * (root - cur -1) / 2)
                        num -= (root - cur-1)
                    else:
                        res += num * (num - 1) / 2
                        #print('add:', num * (num - 1) / 2)
                        num = 1
                    cur = root
        res += num * (num - 1) / 2
        #print('add:', num * (num - 1) / 2)
        return res

if __name__ == '__main__':
     s = Solution()
     A = [3,2,1,2,1,7]
     print(A)
     print(s.minIncrementForUnique(A))
     A = [0,1,1]
     print(A)
     print(s.minIncrementForUnique(A))

