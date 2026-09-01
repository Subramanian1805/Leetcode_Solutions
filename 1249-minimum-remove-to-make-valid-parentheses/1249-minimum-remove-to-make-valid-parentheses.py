class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        remove = [False] * len(s)

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    remove[i] = True

        while stack:
            remove[stack.pop()] = True

        return ''.join(
            ch for i, ch in enumerate(s)
            if not remove[i])