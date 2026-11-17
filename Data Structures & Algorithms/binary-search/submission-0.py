class Solution:

    def search(self, nums: List[int], target: int) -> int:

        if target not in nums:
            return -1
        
        size = len(nums)-1
        first = 0
        last = size
        middle = size//2

        while nums[middle]!=target:

            if target>nums[middle]:
                first = middle+1
                middle = (first+last)//2
                continue
            if target<nums[middle]:
                last = middle-1
                middle = (first+last)//2
                continue
        
        return middle

  