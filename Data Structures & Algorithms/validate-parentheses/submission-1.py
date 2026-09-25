class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if (c == ')' and x != '(') or (c == '}' and x != '{') or (c == ']' and x != '['):
                    return False
            else:
                return False
        
        return len(stack) == 0
