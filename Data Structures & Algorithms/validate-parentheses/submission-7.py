class Solution:
    def isValid(self, s: str) -> bool:

        openBrackets = "{(["
        closeBrackets = ")}]"
        stack = []

        for bracket in s:

            if bracket in openBrackets:
                stack.append(bracket)
                continue
                
            if bracket in closeBrackets:
                if stack==[]:
                    return False
                if bracket==")" and stack[-1]!="(":
                    return False
                if bracket=="}" and stack[-1]!="{":
                    return False
                if bracket=="]" and stack[-1]!="[":
                    return False
                if bracket==")" and stack[-1]=="(":
                    stack.pop()
                    continue
                if bracket=="}" and stack[-1]=="{":
                    stack.pop()
                    continue
                if bracket=="]" and stack[-1]=="[":
                    stack.pop()
                    continue

        if stack==[]:
            return True
        else:
            return False
             
              
             

            




        