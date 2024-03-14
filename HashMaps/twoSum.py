class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in numMap:
                return [numMap[complement], i]
            else:
                numMap[nums[i]] = i

        return []