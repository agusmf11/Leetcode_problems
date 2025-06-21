class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        s = " ".join(s)
        return s

solver = Solution()
print(solver.reverseWords("a good   example"))