class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for n in range(len(nums)):
            seen[nums[n]] = n
        for n in range(len(nums)):
            remain = target - nums[n]
            if remain in seen.keys() and seen.get(remain) != n:
                return [n, seen.get(remain)]
        return []