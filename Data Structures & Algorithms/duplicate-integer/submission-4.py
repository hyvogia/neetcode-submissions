class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicate = set()
        for n in nums:
            if n in seen:
                duplicate.add(n)
            else:
                seen.add(n)
        
        if len(duplicate) > 0:
            return True
        else:
            return False