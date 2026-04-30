class Solution:

    def encode(self, strs: List[str]) -> str:
        str_list_new = []
        for string in strs:
            str_list_new.append(string.replace('&', '-&'))
        strcode = "&".join(str_list_new)
        strcode = "&" + strcode + "&" if strs else ""
        return strcode

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        indices = [i for i, char in enumerate(s) if (i > 0 and s[i] == "&" and (s[i-1] != "-"))]
        res = []
        s1 = s[:]
        cur_idx = 1
        for i, idx in enumerate(indices):
            res.append(s1[cur_idx:idx])
            cur_idx = idx + 1
        for i in range(len(res)):
            res[i] = res[i].replace('-&', '&')
        return res
        