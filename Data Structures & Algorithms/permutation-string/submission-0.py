class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        require = {}
        for s in s1:
            require[s] = 1 + require.get(s,0)

        seen = {}
        l,r = 0,0
        while l < (len(s2) - len(s1)+1):
            if s2[l] in s1:
                seen[s2[l]] = 1 + seen.get(s2[l],0)
                r = l
                for r in range(1,len(s1)):
                    seen[s2[l+r]] = 1 + seen.get(s2[l+r],0)
                if seen == require:
                    return True
                seen = {}
            l += 1
        return False



        