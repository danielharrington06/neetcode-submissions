class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op not in "+CD":
                record.append(int(op))
            elif op == "C":
                record.pop()
            elif op == "D":
                record.append(record[-1]*2)
            elif op == "+":
                record.append(record[-2] + record[-1])
        
        return sum(record)