class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = []
        for sub in grid:
            for n in sub:
                if n < 0:
                    negatives.append(n)
        return len(negatives)
