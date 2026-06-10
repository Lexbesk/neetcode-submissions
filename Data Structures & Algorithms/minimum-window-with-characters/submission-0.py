class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1
        count = {}
        cur_letter = ""
        present_num = 0
        min_len = len(s)
        ans = ""

        left = 0
        
        for right in range(len(s)):
            count[s[right]] = count[s[right]] + 1 if s[right] in count else 1
            if (s[right] in t) and (count[s[right]] <= count_t[s[right]]):
                present_num += 1
            if present_num < len(t):
                continue
            
            while ((s[left] not in t) or (s[left] in t and count[s[left]] > count_t[s[left]])):
                count[s[left]] = count[s[left]] - 1 if count[s[left]] > 0 else 0
                left += 1
            
            if right + 1 - left <= min_len:
                ans = s[left:right+1]
                min_len = right + 1 - left
        
        return ans






