class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        self.check = [(c+extraCandies) for c in candies]
        self.max = max(candies)
        bools = [True if c >=self.max else False for c in self.check] 
        return bools
