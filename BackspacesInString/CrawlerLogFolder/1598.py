class Solution:
    def minOperations(self, logs: List[str]) -> int:
        min_op=0

        for op in logs:
            if op == "../"   :
                if min_op != 0:
                    min_op -= 1
            elif op == "./":
                continue
            else:
                min_op += 1
        
        return min_op


        