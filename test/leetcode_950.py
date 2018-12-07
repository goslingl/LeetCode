# error

import math

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        num = len(deck)
        res = [0] * num
        round = math.ceil(math.log2(num))
        flag = 0
        map = {}
        for rnd in range(round+1):
            for idx in range(num):
                if ((idx + 1) / (2 ** rnd)) % 2 == 1:
                    map[idx] = flag
                    #print('rnd, idx+1, flag',rnd, idx+1, flag)
                    flag += 1
        #print(map)
        for idx in map:
            res[idx] = deck[map[idx]]
        return res

if __name__ == '__main__':
    s = Solution()
    deck = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
    print(deck, s.deckRevealedIncreasing(deck))
    deck = [ 1, 2, 3, 4, 5, 6, 7 ]
    print(deck, s.deckRevealedIncreasing(deck))
