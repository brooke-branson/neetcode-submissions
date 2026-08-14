class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        res = []
        nums.sort()
        for i in range(len(nums)):
            l = 1 + i
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    candidate = [nums[i], nums[l], nums[r]]
                    if candidate not in res:
                        res.append(candidate)
                    l += 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
            
        return res