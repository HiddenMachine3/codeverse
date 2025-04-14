class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        freq_map = {i:0 for i in set(nums)}
        for i in nums:
            freq_map[i] += 1
            if freq_map[i] > n/2:
                return i