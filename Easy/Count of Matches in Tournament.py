class Solution:
    def numberOfMatches(self, n: int) -> int:
        def match(n):
            matches = 0
            advance = 0
            if n % 2 == 0:
                matches = n /2
                advance = n / 2
                n = (n-advance)
            else:
                matches = (n-1) / 2
                advance = ((n-1) / 2) + 1
                n = (n - advance) + 1
            return [matches,advance]
        
        final = []
        while n >=2:
            matches = match(n)[0]
            final.append(matches)
            n = match(n)[1]
            
        return int(sum(final))
                
