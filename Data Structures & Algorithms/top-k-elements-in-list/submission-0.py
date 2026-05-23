class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = Counter(nums)
        res = dict(sorted(result.items(), key = lambda x: x[1], reverse = True)[:k])
        final = list(res.keys())
        return final 
        