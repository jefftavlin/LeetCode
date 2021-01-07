class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = sorted([n ** 2 for n in nums])
        return result
