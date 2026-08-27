class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = defaultdict(list)
        for s in strs:
            c = [0] * 26
            for v in s:
                c[ord(v) - ord("a")] += 1 
            k = tuple(c)
            r[k].append(s)
        return list(r.values())