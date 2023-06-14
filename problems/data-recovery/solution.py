from typing import List


def recover_data(lines: List[str]) -> str:
    result = ''

    line_length = len(lines[0])
    for c in range(line_length):
        counts: dict[str, int] = {}
        for line in lines:
            char = line[c]
            if char != " ":
                counts[char] = counts.get(char, 0) + 1

        if len(counts) == 0:
            result += " "
        else:
            char = max(counts, key=counts.get)
            result += char

    return result

line_count = int(input())
lines = [input()[1:-1] for _ in range(line_count)]
recovered = recover_data(lines)
print(recovered)
