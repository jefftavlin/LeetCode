class Solution:
    def numJewelsInStones(self, J, S):
        J = [c for c in J]
        S = [c for c in S]
        count = [c for c in S if c in J]
        return len(count)
        
