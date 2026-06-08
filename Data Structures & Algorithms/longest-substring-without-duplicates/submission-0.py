class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_chars = set()
        l = len(s)
        i = 0
        j = 0
        max_l = 0
        while j < l:
            if s[j] in cur_chars:
                cur_chars.remove(s[i])
                i += 1
            else:
                cur_chars.add(s[j])
                j += 1
                max_l = max(max_l, j - i)
        return max_l
                