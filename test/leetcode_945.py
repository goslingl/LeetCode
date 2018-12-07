# 超时
class Solution:
    def minIncrementForUnique(self, A):
        res = 0
        if len(A) <= 1:  return res
        H = [len(A)] + A # build heap
        self.build_heap(H)
        #print(H)
        cur, num = -1, 0
        while H[0] > 0:
            (root, H) = self.delete(H)
            #print("res, root, cur, num:", res, root, cur, num)
            #print("(root, H):", root, H)
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

    def _heap(self, H, idx):
        if H[0]-idx < 1 or H[0]/2 < idx: return
        left = 2 * idx
        right = 2 * idx + 1
        min_idx = left if H[idx] > H[left] else idx
        min_idx = right if right <= H[0] and H[min_idx] > H[right] else min_idx
        if min_idx != idx:
            H[idx], H[min_idx] = H[min_idx], H[idx]
            self._heap(H, min_idx)

    def build_heap(self, H):
        for idx in xrange(H[0]/2, 0, -1):
            self._heap(H, idx)
            #print(idx, H)

    def delete(self, H):
        root = H[1]
        H[1] = H[H[0]]
        H = H[:H[0]] 
        H[0] -= 1
        self._heap(H, 1)
        return (root, H)

if __name__ == '__main__':
     s = Solution()
     A = [3,2,1,2,1,7]
     #print(A)
     #print(s.minIncrementForUnique(A))
     A = [0,1,1]
     #print(A)
     #print(s.minIncrementForUnique(A))

