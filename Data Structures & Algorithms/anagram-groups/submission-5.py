class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_map = dict()
        for i in range(len(strs)):
            az_str = ''.join(sorted(list(strs[i])))
            re_str = strs[i]
            if az_str in a_map:
                a_map[az_str].append(re_str)
            else:
                a_map[az_str] = [re_str]
        return list(a_map.values())