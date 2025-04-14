class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bubble sort
        for j in range(len(nums)-1,-1,-1):
            for k in range(j):
                if nums[k] > nums[k+1]:
                    nums[k], nums[k+1] = nums[k+1], nums[k]