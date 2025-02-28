class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=''.join(sorted(s))
        n=''.join(sorted(t))
        if m == n:
            return True
        else:
            return False
        