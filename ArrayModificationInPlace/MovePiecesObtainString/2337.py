class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i, j = 0, 0

        while i < n or j < n:
            # 1. Skip underscores in start
            while i < n and start[i] == '_':
                i += 1
            
            # 2. Skip underscores in target
            while j < n and target[j] == '_':
                j += 1

            # 3. Check if one reached end and the other didn't
            if i == n or j == n:
                return i == n and j == n

            # 4. Pieces must be the same character
            if start[i] != target[j]:
                return False

            # 5. Movement constraints
            # L can only move left (i >= j)
            if start[i] == 'L' and i < j:
                return False
            # R can only move right (i <= j)
            if start[i] == 'R' and i > j:
                return False

            # Move to next characters
            i += 1
            j += 1

        return True