class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if t == "":
            return ""
        # set-up
        countT, window = {},{}
        resLen = float("infinity")
        res = [-1,-1]
        l = 0
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        have, need = 0, len(countT)
        # start
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need: 
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l,r]
                
                left = s[l]
                window[left] = window.get(left,0) - 1
                if left in t and countT[left] > window[left]:
                    have -= 1
                l += 1
        l,r = res[0], res[1]
        return s[l:r+1] if resLen != float("infinity") else ""




            
        