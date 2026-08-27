class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i,num in enumerate(nums):
            v = target - num
            if v in s:
                return [s[v],i]
            else:
                s[num] = i