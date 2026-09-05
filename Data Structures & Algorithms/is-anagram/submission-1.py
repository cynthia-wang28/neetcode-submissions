class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        for char in s:
            s1[char] = 1 + s1.get(char, 0)
            
        for char in t:
            s2[char] = 1 + s2.get(char, 0)
        
        return s1 == s2
