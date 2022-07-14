class Solution:
    def isValid(self, s: str) -> bool:
        point = {'(':')', '[':']','{':'}'}
        stack = []
       
        for v,i in enumerate(s):
            
            if i in point and v != len(s) - 1:
                
                stack.append(i)
            else:
                if stack:
                    if i != point[stack.pop()]:
                        return False
                  
                else:
                    return False
                
                if stack and v == len(s)-1:
                    return False
           
        return True