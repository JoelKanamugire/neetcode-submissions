class Solution:
    def isValid(self, s: str) -> bool:
        validpairs = ['()', '{}', '[]']
        openchars = ['(', '{', '[']
        stack = []

        for char in s:
            if char in openchars:
                stack.append(char)
            else:
                if not stack or stack[-1] + char not in validpairs:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False
      