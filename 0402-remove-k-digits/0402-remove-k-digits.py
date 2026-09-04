class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:
            while k and stack and stack[-1] > c:
                stack.pop()
                k -= 1

            stack.append(c)

        if k:
            stack = stack[:-k]

        result = ''.join(stack).lstrip('0')

        return result or '0'