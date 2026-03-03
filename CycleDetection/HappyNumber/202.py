class Solution:
    def isHappy(self, n):
        def f(x):
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s
        
        slow = n
        fast = f(n)
        while fast != 1 and slow != fast:
            slow = f(slow)
            fast = f(f(fast))
        return fast == 1