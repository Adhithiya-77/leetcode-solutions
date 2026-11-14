class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while stack and stack[-1]>digit and k>0:
                stack.pop()
                k-=1
            stack.append(digit)

        while k>0:
            stack.pop()
            k-=1

        s = "".join(stack).lstrip("0")
        return "0" if not s else s            

        