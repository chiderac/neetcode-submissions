class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if seen.get(complement) == None:
                seen[num] = i
            else:
                return [seen[complement], i]
                