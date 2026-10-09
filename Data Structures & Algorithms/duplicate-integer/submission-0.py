class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsCount = []

        for num in nums:
            if num not in numsCount:
                numsCount.append(num)
            else:
                return True
        return False