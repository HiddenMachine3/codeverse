class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        l_r_map = {'(':')', '{':'}', '[':']'}
        r_l_map = {r:l for l,r in l_r_map.items()}
        for c in list(s):
            if c in l_r_map.keys():
                stack.append(c)
            else:
                if stack:
                    if r_l_map[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
        
        return True if not stack else False