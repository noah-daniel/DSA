class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for num in nums:
            if num in vals:
                return True
            else:
                vals[num] = 0
        return False
        