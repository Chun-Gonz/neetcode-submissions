class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        sCount = {}
        for char in s:
            if char not in sCount:
                sCount[char]=1
            else:
                sCount[char]+=1

        for char in sCount:
            if char not in t:
                return False
            if sCount[char]!=t.count(char):
                return False
            
        return True
        
   
        

        