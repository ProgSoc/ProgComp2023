from typing import List


def recover_data(lines: List[str]) -> str:
    # Your code goes here
    return ""

line_count = int(input())
lines = [input()[1:-1] for _ in range(line_count)]
recovered = recover_data(lines)
print(recovered)
