from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        max_len = max(map(len, words), default=0)

        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return [""]

            result = []

            for j in range(i + 1, min(len(s), i + max_len) + 1):
                word = s[i:j]

                if word in words:
                    for suffix in dfs(j):
                        result.append(word if not suffix else word + " " + suffix)

            return result

        return dfs(0)