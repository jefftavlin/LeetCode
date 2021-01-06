class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = []
        def get_max_right(arr,position):
            sliced = arr[position+1:]
            top = max(sliced)
            return top
        for i in range(len(arr)-1):
            right = get_max_right(arr,i)
            l.append(right)
        l.append(-1)
        return l
