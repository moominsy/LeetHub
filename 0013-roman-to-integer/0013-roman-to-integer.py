class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        for i in range(len(s)):
            if i==0:
                res += d[s[i]]
                continue
            curr, prev = s[i], s[i-1]
            if ((curr == "V" or curr == "X") and prev== "I") or \
                ((curr == "L" or curr == "C") and prev== "X") or \
                ((curr == "D" or curr == "M") and prev== "C"):
                res += d[curr] - 2 *  d[prev]
                

            else:
                res += d[s[i]]
            print(res)
        return res