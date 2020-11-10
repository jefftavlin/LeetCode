class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = Counter(nums).most_common()[::-1][0][0]
        return num
