class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortedArray = sorted(nums)
        for current, next_val in zip(sortedArray, sortedArray[1:]):
            if current == next_val:
                return True 
        return False
        