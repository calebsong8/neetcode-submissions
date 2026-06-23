class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {']':'[', '}':'{', ')':'('}

        for e in s:
            if e in closeToOpen:
                if stack and stack[-1] == closeToOpen[e]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(e)
        
        return True if not stack else False