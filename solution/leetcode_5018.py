import re

class Solution:
    def countUpper(self, s):
        num = 0
        for c in s:
            if c.isupper(): num += 1
        return num

    def filtered(self, q, p):
        pset = set(p)
        res = ''
        for c in q:
            if c in pset: res += c
        return res

    def splitPart(self, p):
        res = []
        part = ''
        for c in p:
            if c.isupper():
                if part != '':
                    res.append(part)
                part = c
            else:
                part += c
        res.append(part)
        return res

    #def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
    def camelMatch(self, queries, pattern):
        res = [ True ] * len(queries)
        for qidx in range(len(queries)):
            if self.countUpper(queries[qidx]) != self.countUpper(pattern):
                res[qidx] = False
                continue
            q = self.filtered(queries[qidx], pattern)
            #parts = self.splitPart(pattern)
            parts = list(pattern)
            pos_list = []
            for part in parts:
                if q.find(part) < 0:
                    res[qidx] = False
                    break
                pos = [ m.start() for m in re.finditer(part, q)]
                if part.isupper():
                    if len(pos) != len([m.start for m in re.finditer(part, pattern)]):
                        res[qidx] = False
                        break
                pos_list.append(pos)
            if res[qidx] == False: continue
            if len(pos_list) == len(parts):
                last = -1
                for pos in pos_list:
                    for idx in range(len(pos)):
                        if pos[idx] > last:
                            last = pos[idx]
                            break
                    else:
                        res[qidx] = False
                        break
                    print('last:', last)
                print('<-------end last')
                print('idx:', qidx, 'res:', res[qidx])
        return res

def main():
    s = Solution()
    queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]; pattern = "FB"
    print(s.camelMatch(queries, pattern))
    queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]; pattern = "FoBa"
    print(s.camelMatch(queries, pattern))
    queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]; pattern = "FoBaT"
    print(s.camelMatch(queries, pattern))
    queries = ["CompetitiveProgramming","CounterPick","ControlPanel"]; pattern = "CooP"
    print(s.camelMatch(queries, pattern))


main()

