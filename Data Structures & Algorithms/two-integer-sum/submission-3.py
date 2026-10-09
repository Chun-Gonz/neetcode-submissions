class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        size = len(nums)
        result = []

        for i in range(0, size-1):
            for j in range(i+1, size):
                if nums[i]+nums[j]==target:
                    result.extend([i, j])
                    return result
        



        