class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hsst = set()
        for num in nums:
            if num in hsst:
                return True
            hsst.add(num)
        return False