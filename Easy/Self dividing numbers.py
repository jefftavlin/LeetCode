class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = list(range(left,right+1))
        good = []
        for n in l:
            length = len(str(n))
            count = 0
            k = str(n)
            if '0' not in k:   
                for i in range(length):
                    if n % int(k[i]) == 0:
                        count += 1
                    else:
                        break
                if count == length:
                    good.append(n)
        return good
