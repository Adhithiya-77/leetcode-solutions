class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        count = 0
        for i in range(n):
            count += self.expand(s, i, i, n)
            count += self.expand(s, i, i + 1, n)
        return count

    def expand(self, s, left, right, n):
        count = 0
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count