from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        mid = ""

        total = 0
        for c in range(26):
            ch = chr(ord('a') + c)
            half[c] = freq[ch] // 2
            total += half[c]
            if freq[ch] % 2:
                mid = ch

        # Exact number of distinct permutations of the half-multiset.
        # No capping here -- we need the EXACT value for the
        # reconstruction step below to give correct ratios.
        def countWays(cnt):
            ways = 1
            used = 0
            for f in cnt:
                if f:
                    ways *= comb(used + f, f)
                    used += f
            return ways

        ways = countWays(half)
        if ways < k:
            return ""

        left = []
        for pos in range(total):
            rem = total - pos
            for c in range(26):
                if half[c] == 0:
                    continue
                nxt = ways * half[c] // rem  # exact, since ways is exact
                if nxt >= k:
                    left.append(chr(ord('a') + c))
                    half[c] -= 1
                    ways = nxt
                    break
                else:
                    k -= nxt

        left_str = "".join(left)
        return left_str + mid + left_str[::-1]