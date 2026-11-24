class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num]=0
            else:
                counts[num]+=1
        for value in counts.values():
            if value > 0:
                return True
        return False
