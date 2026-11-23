class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if stack and i == "*":
                stack.pop()

            else:
                stack.append(i)

        result = ""

        for i in stack:
            result+=i

        return result             
        