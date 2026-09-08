class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            temp = nums[i]
            res[i] *= prefix
            prefix *= temp

        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            temp = nums[i]
            res[i] *= suffix
            suffix *= temp
        return res

        