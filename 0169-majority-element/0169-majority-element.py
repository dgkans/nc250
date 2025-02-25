class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        dict_count = {}
        for i in nums:
            dict_count[i] = dict_count.get(i,0)+1
        maj_elekey = max(dict_count,key = dict_count.get)
        if dict_count[maj_elekey] > n:
            return maj_elekey
            