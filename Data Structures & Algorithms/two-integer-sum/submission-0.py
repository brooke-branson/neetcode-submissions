class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for k, v in enumerate(nums):
            need = target - v
            if need in seen:
                return [seen[need], k]
            else:
                seen[v] = k
