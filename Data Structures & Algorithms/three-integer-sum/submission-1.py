class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

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
                elif total > target:
                    r -= 1
                else:
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

            
        return res