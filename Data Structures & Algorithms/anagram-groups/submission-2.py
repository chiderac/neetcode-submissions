class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         strs2 = list(map(lambda x: "".join(sorted(x)),strs))
         indices = list(range(len(strs)))
         g = groupby(sorted(indices, key=lambda i: strs2[i]), key=lambda i: strs2[i])
         result = [[strs[i] for i in group] for _, group in g]
         return result
        