class Solution:
    def shuffle(self, nums, n):
        list_one = nums[0:n]
        list_two = nums[n:]
        list_three = []
        
        i = 0
        while i < n:
            list_three.append(list_one[i])
            list_three.append(list_two[i])
            i +=1
        return list_three
