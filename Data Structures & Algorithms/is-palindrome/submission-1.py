class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        i = 0
        while i < len(s_lower):
            if not s_lower[i].isalnum():
                s_lower = s_lower[:i] + s_lower[i+1:]
            else:
                i += 1
        return s_lower == s_lower[::-1]