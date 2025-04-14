class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge cases

        if len(nums)<=1:
            return len(nums)

        nums.sort()

        longest_seq_len = 0

        curr_len = 1

        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                curr_len += 1
            elif nums[i]==nums[i-1]:
                continue
            else:
                longest_seq_len = max(longest_seq_len, curr_len)
                curr_len = 1
        longest_seq_len = max(longest_seq_len, curr_len)

        return longest_seq_len