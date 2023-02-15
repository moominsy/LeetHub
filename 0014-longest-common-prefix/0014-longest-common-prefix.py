class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len) # shortest str in strs
        ret = ""
        for idx in range(len(shortest)):
            for word in strs:
                if shortest[idx] != word[idx]:
                    return ret
            ret += shortest[idx]
        return ret

        