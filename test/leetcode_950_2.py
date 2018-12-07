# pass

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        num = len(deck)
        raw = list(range(num))
        map = {}
        res = []
        fres = []
        st = 0
        ed = num - 1
        while len(res) < num:
            res.append(raw[st])
            next = (st+1)%num
            ed = (ed+1)%num
            raw[ed] = raw[next]
            if st != ed: raw[st] = -1
            if next != ed: raw[next] = -1
            st = (st+2)%num
        for idx in range(num):
            map[res[idx]] = deck[idx]
        for idx in range(num):
            fres.append(map[idx])
        return fres

if __name__ == '__main__':
    s = Solution()
    deck = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
    print(deck, s.deckRevealedIncreasing(deck))
    deck = [ 1, 2, 3, 4, 5, 6, 7 ]
    print(deck, s.deckRevealedIncreasing(deck))
    deck = [17,13,11,2,3,5,7]
    print(deck, s.deckRevealedIncreasing(deck))
