class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs_map = dict()
        for i in range(len(nums)):
            if nums[i] in hs_map:
                hs_map[nums[i]].append(nums[i])
            else:
                hs_map[nums[i]] = [nums[i]]
        fq_list = []
        for key, value in hs_map.items():
            fq_list.append([len(value), key])
        fq_list.sort()
        res = []
        for i in range(k):
            res.append(fq_list.pop()[1])
        return res