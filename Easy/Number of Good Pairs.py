class Solution:
    def numIdenticalPairs(self, nums):
        a = [[i,nums[i]] for i in range(len(nums))]
        good = 0
        for i in range(len(a)):
            for j in range(len(a)):
                if a[i][1] == a[j][1] and a[i][0] < a[j][0]:
                    good +=1
        return good
