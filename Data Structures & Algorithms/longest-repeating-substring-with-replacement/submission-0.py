class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_window = 0
        counts = {}
        max_freq = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_freq = max(max_freq, counts[s[r]])

            while (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1

            max_window = max(max_window, r - l + 1)

        return max_window


