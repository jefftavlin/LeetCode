import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = collections.Counter(arr)
        counts = [item[1] for item in counts.items()]
        final = [counts.count(n) for n in counts]
        for n in final:
            if n > 1:
                return False
        return True
