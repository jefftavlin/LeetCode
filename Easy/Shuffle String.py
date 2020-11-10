class Solution:
    def restoreString(self, s, indices):
        combined = [[s[i], indices[i]] for i in range(len(s))]
        combined = [c[0] for c in sorted(combined, key = lambda x: x[1])]
        return ''.join(combined)
