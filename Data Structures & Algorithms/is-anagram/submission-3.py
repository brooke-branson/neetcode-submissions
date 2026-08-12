class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = self.get_hash(s)
        for i in t:
            if i not in hash_map:
                return False
            else:
                if hash_map[i] > 0:
                    hash_map[i] -= 1
                else:
                    return False
        return True

    def get_hash(self, s):
        hash_map = {}
        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        return hash_map 