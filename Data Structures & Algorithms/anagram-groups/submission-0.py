class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            output[sorted_s].append(s)
        return list(output.values())
        