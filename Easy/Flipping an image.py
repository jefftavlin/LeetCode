class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def flip_image(arr):
            B = []
            for sub in arr:
                B.append(sub[::-1])
            return B
        B = flip_image(A)
        
        def invert_image(arr):
            C = []
            for sub in arr:
                D = []
                for pixel in sub:
                    if pixel == 0:
                        D.append(1)
                    elif pixel == 1:
                        D.append(0)
                C.append(D)
            return C
        C = invert_image(B)
        return C
