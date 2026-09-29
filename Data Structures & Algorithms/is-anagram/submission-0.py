class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_s = {}
        char_t = {}

        for char in s:
            if char in char_s:
                char_s[char] += 1
            else:
                char_s[char] = 1

        for char in t:
            if char in char_t:
                char_t[char] += 1
            else:
                char_t[char] = 1

        return char_s == char_t