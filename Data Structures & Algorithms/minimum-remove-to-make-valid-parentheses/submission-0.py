class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removeIdx = []
        for index, item in enumerate(s):
            if item == '(':
                stack.append(index)
            if item == ')':
                if len(stack) == 0:
                    removeIdx.append(index)
                else:
                    stack.pop()

        removeIdx = removeIdx + stack
        result = []
        for index, item in enumerate(s):
            if index not in removeIdx:
                result.append(item)

        return "".join(result)