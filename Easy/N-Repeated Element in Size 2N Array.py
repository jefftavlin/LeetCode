class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counts = []
        for n in A:
            if A.count(n) > 1:
                counts.append(n)
                break
        return counts[0]
