class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            # print(sorted_word)
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
            # print(word, sorted_word, anagram_dict)
        
        res = []
        for key in anagram_dict:
            res.append(anagram_dict[key])

        return res