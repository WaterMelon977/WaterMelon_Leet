class Solution:
    def minimumSteps(self, s: str) -> int:
        n=len(s)

        moves=0
        one_count=0

        for i in range(n):
            if s[i] == '1':
                one_count += 1
            else:
                moves += one_count
        return moves

        