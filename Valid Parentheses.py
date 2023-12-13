class Solution(object):
    def isValid(self, s):
        open_brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for element in s:
            if element in '([{':
                stack.append(element)
            elif len(stack) == 0 or element != open_brackets[stack[0]]:
                stack.pop()
                return False
        return len(stack) == 0
    
s = "(]"
sol = Solution()
print(sol.isValid(s))