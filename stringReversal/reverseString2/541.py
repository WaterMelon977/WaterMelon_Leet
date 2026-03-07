class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ls =list(s)
        n=len(s)
        times = (n-1)//(2*k)

        for i in range(times+1):
            L =i*2*k
            R =min(( i*2*k) + k - 1,n-1)
            while L<R:
                ls[L],ls[R] =ls[R],ls[L]
                L += 1
                R -= 1
        return ''.join(ls)

            

