class Solution:

  def longestPalindrome(self, s: str) -> str:
    if not s:
      return ""

    start = 0
    end = 0
    n = len(s)

    for i in range(n):
      len1 = self.expand(s, i, i)
      len2 = self.expand(s, i, i + 1)  # Fixed: passed both i and i + 1
      length = max(len1, len2)

      if length > (end - start):
        start = i - (length - 1) // 2
        end = i + length // 2

    return s[start : end + 1]

  def expand(self, s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    return right - left - 1