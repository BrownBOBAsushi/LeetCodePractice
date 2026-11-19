class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Your implementation
        counts = {}

        for char_s in s:
            if char_s in counts:
                counts[char_s] += 1
            else:
                counts[char_s] = 1

        for char_t in t:
            if char_t in counts:
                counts[char_t] -= 1
            else:
                return False

        for count in count.values():
            if count != 0:
                return False
        return True