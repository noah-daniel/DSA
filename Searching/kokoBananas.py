import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        hi = max(piles)

        while low <= hi:
            mid = (low + hi) // 2
            if self.canEat(piles, h, mid):
                hi = mid - 1
            else:
                low = mid + 1
        
        return low

    
    def canEat(self, piles, h, k):
        time_left = h
        success = True
        for pile in piles:
            time_left -= math.ceil(pile / k)
            if time_left < 0:
                success = False
                break
        return success