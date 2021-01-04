class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l = [len(str(n)) for n in nums if len(str(n)) % 2 == 0]
        return len(l)
