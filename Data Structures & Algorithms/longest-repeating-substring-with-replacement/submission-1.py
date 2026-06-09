class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_frequency = 0
        ans = 0

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
            max_frequency = max(max_frequency, count[s[right]])

            while right - left + 1 - max_frequency > k:
                count[s[left]] = count[s[left]] - 1 if count[s[left]] > 0 else 0
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans