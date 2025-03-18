class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1
        for num in nums:
            if num > min_val:
                diff = num - min_val
                max_diff = max(diff,max_diff)
            else:
                min_val = num
        if max_diff != 0:
            return max_diff
        else:
            return -1