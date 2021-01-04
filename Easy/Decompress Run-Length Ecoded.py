class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n  = 2
        l = [nums[i * n:(i + 1) * n] for i in range((len(nums) + n - 1) // n )]
        final = []
        for chunk in l:
            final.append(chunk[0] * [chunk[1]])
        flat_list = [item for sublist in final for item in sublist]
        return flat_list
