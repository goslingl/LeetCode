
class Solution:
    def inRange(self, p, q):
        if q[0] <= p[1] and q[0] >= p[0] and q[1] <= p[1] and q[1] >= p[0]:
            return True
        return False

    def border(self, p, q):
        if q[0] <= p[1] and q[0] >= p[0]:
            return True
        return False

    #def videoStitching(self, clips: List[List[int]], T: int) -> int:
    def videoStitching(self, clips, T):
        clips = sorted(clips)
        flags = [ True ] * len(clips)
        # filter
        for idx in range(len(clips)):
            if clips[idx][1] > T: clips[idx][1] = T
            for idx2 in range(idx+1, len(clips)):
                if flags[idx2]:
                    if self.inRange(clips[idx], clips[idx2]):
                        flags[idx2] = False
                    elif self.inRange(clips[idx2], clips[idx]):
                        flags[idx] = False
        # splice
        st = T
        ed = -1
        last = [ 0, 0 ]
        last_max = 0
        max_idx = -1
        res = []
        for idx in range(len(clips)):
            if flags[idx]:
                if self.border(last, clips[idx]) == False:
                    if max_idx >= 0:
                        print(clips[max_idx])
                        res.append(max_idx)
                        last = clips[max_idx]
                        if clips[max_idx][0] < st: st = clips[max_idx][0]
                        if clips[max_idx][1] > ed: ed = clips[max_idx][1]
                        max_idx = -1
                if clips[idx][1] > last_max:
                    last_max = clips[idx][1]
                    max_idx = idx
                    if last_max >= T: break
        if max_idx >= 0:
            print(clips[max_idx])
            res.append(max_idx)
            last = clips[max_idx]
            if clips[max_idx][0] < st: st = clips[max_idx][0]
            if clips[max_idx][1] > ed: ed = clips[max_idx][1]
        #print(res, st, ed)
        if st == 0 and ed == T:
            return len(res)
        else:
            return -1

def main():
    s = Solution()
    clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]; T = 10
    s.videoStitching(clips, T)
    clips = [[0,1],[1,2]]; T = 5
    s.videoStitching(clips, T)
    clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]; T = 9
    s.videoStitching(clips, T)
    clips = [[0,4],[2,8]]; T = 5
    s.videoStitching(clips, T)

main()
