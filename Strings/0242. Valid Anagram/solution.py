class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for i in s:
            count[i] = count.get(i, 0) + 1

        for j in t:
            count[j] = count.get(j, 0) - 1

        return all(v == 0 for v in count.values())