class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()
        for i in range(len(nums)):
            num_map[nums[i]] = i
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in num_map and num_map.get(remain) != i:
                return [i, num_map.get(remain)]
        return []