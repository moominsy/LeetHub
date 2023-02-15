class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_dict = dict()
        for i in range(len(s)):
            c = s[i]
            if c in map_dict:
                if map_dict[c] != t[i]:
                    return False
            else:
                if t[i] in map_dict.values():
                    return False
                map_dict[c] = t[i]
        return True