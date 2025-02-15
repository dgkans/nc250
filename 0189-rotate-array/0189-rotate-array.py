class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[n-k:] = reversed(nums[n-k:])
        nums[:n-k] = reversed(nums[:n-k])
       
        nums[:] = reversed(nums[:])          
        return nums   