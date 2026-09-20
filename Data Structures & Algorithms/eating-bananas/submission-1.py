class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) # this gives the minimum time which has to <= h
        while l < r:
            k = (l + r) // 2
            t = 0
            for i in range(len(piles)):
                t += piles[i] // k
                if piles[i] - (piles[i] // k) * k > 0:
                    t += 1
            if t <= h:
                r = k
            else:
                l = k + 1
        return l

        