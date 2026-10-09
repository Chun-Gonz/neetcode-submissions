class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        sCount = {}
    
        for sChar in s:
            if sChar not in sCount:
                sCount[sChar]=1
            else:
                sCount[sChar]+=1

        for i in sCount:
            if i not in t:
                return False
            if t.count(i)!=sCount[i]:
                return False
        return True

        
   
        

        