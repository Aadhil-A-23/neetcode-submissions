class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        v = []
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key,value in hash.items():
            bucket[value].append(key)
        for i in range(len(bucket)-1, -1, -1):
            for b in bucket[i]:
                v.append(b)
                if len(v) == k:
                    return v