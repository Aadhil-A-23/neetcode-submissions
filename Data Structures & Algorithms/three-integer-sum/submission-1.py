class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        result = []
        for i in range(len(num)):
            # Skip duplicate i values
            if i > 0 and num[i] == num[i - 1]:
                continue
            l = i + 1
            r = len(num) - 1
            while l < r:
                v = num[i] + num[l] + num[r]
                if v < 0:
                    l += 1
                elif v > 0:
                    r -= 1
                else:
                    result.append([num[i], num[l], num[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate left values
                    while l < r and num[l] == num[l - 1]:
                        l += 1
                    # Skip duplicate right values
                    while l < r and num[r] == num[r + 1]:
                        r -= 1
        return result