class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totals = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            totals[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            totals[i] *= postfix
            postfix *= nums[i]
            
        return totals

