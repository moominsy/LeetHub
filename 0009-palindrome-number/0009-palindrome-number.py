class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = len(s)
        for i in range(l):
            if s[i] != s[l-(i+1)]:
                return False

        return True