class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        l = 0
        for num in nums:
            if num-1 not in num_set:
                c = 1
                while num+1 in num_set:
                    c+=1
                    num+=1
                l = max(l,c)
        return l