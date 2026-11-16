class Solution:
    def isPalindrome(self, s: str) -> bool:
   
        allow = "1234567890abcdefghijklmnopqrstuvwxyz"
        lowercase_s = s.lower()
        new_lower_s = ""

        for char in lowercase_s:
            if char in allow:
                new_lower_s+=char
            else:
                continue

        start = 0
        end = len(new_lower_s)-1

        while start<=end:
            if new_lower_s[start]==new_lower_s[end]:
                start+=1
                end-=1
                continue
            else:
                return False
        return True


        

        


    

