class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hashmap approach: hashmaps comparisons work regardless of order

        s_Hashmap = {}
        
        for i in range(len(s)):
            if s[i] in s_Hashmap:
                s_Hashmap[s[i]] += 1
            else:
                s_Hashmap[s[i]] = 1
        
        t_Hashmap = {}
        
        for i in range(len(t)):
            if t[i] in t_Hashmap:
                t_Hashmap[t[i]] += 1
            else:
                t_Hashmap[t[i]] = 1  
                
        return s_Hashmap == t_Hashmap