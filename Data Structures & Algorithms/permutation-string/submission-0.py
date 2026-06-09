class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        for char in s1:
            if char in count_s1:
                count_s1[char] += 1
            else:
                count_s1[char] = 1
        
        count = {}
        left = 0

        for right in range(len(s2)):
            if s2[right] not in count_s1:
                left = right + 1
                count = {}
                continue
            
            count[s2[right]] = count[s2[right]] + 1 if s2[right] in count else 1
            while count[s2[right]] > count_s1[s2[right]]:
                count[s2[left]] = count[s2[left]] - 1 if count[s2[left]] > 0 else 0
                left += 1
            if len(s1) == right - left + 1:
                return True
        
        return False