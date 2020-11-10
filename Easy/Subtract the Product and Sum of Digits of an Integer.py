import numpy as np

class Solution:
    def subtractProductAndSum(self, n):
        l = [int(c) for c in str(n)]
        return np.prod(l) - sum(l)
