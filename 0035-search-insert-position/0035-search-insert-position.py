class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        # left = 0
        # right= len(nums)-1
        # while(left<=right):
        #     mid = left + right // 2 
        #     if target == nums[mid]:
        #         return mid
        #     elif nums[mid] > target:
        #         right = mid-1
        #     else:
        #         left= mid + 1
        # return left

        