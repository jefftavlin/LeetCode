class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bad = []
        for word in words:
            for c in word:
                if c not in allowed:
                    bad.append(word)
                    break
        return len(words) - len(bad)
