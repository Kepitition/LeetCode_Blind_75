#Blind 75 -- 1/75

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                if nums.index((target-nums[i])) != i:
                    return i,nums.index((target-nums[i]))