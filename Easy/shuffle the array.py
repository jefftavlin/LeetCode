class Solution:
    def shuffle(self, nums, n):
        one = nums[:n]
        two = nums[n:]
        three = []
        
        i = 0
        while i < n:
            three.append(one[i])
            three.append(two[i])
            i +=1
        return three
