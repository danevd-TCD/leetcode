class Solution:
    def isPalindrome(self, s: str) -> bool:

        s2 = ""
        
        for i in s:
            if i.isalpha():
                s2 += i.lower()
        
        if len(s2) < 2:
            return False
        
        if len(s2) % 2 != 0:
            midpoint = int(len(s2) // 2)
            half1 = s2[:midpoint]
            half2 = s2[len(s):midpoint:-1] 
        else:
            midpoint = int(len(s2) / 2) -1
            half1 = s2[:midpoint+1]
            half2 = s2[len(s):midpoint:-1]
        
        print(half1)
        print(half2)
        
        return half1 == half2