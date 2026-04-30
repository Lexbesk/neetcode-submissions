class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_s = {}
        char_count_t = {}
        for char in s:
            char_count_s[char] = char_count_s[char] + 1 if char in char_count_s else 1
        for char in t:
            char_count_t[char] = char_count_t[char] + 1 if char in char_count_t else 1
        return char_count_s == char_count_t