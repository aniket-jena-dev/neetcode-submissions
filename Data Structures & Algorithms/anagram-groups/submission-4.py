class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if not hm.get(sorted_s):
                hm[sorted_s] = [s]
            else:
                hm[sorted_s].append(s)
        
        res = []
        for v in hm.values():
            res.append(v)
        
        return res