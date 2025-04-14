class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1

        modified = [(nums[orig_i], orig_i) for orig_i in range(len(nums))]
        modified.sort(key=lambda item:item[0])
        while l < r:
            tot_sum = modified[l][0] + modified[r][0]
            if tot_sum < target:
                l += 1
            elif tot_sum > target:
                r -= 1
            else:
                break

        return [modified[l][1],modified[r][1]]