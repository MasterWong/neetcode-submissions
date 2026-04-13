class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ["{", "[", "("]
        right = {"}" : "{", "]" : "[", ")" : "("}
        for brace in s:
            if brace in left:
                stack.append(brace)
            else:
                if len(stack) >= 1:
                    if stack[-1] == right[brace]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(stack) != 0:
            return False
        else:
            return True