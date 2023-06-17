def broken_sequence(wall: str) -> int:
    count = 0

    for i in range(len(wall) - 1):
        pair = wall[i : i + 2]

        if pair == "RG" or pair == "GB" or pair == "BR":
            continue
        else:
            count += 1

    return count


text = input()
print(broken_sequence(text))
