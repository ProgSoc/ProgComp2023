import random


def randomize_char(c):
    if c == " ":
        return " "

    replace_with_space = random.random() < 0.5
    if replace_with_space:
        return " "
    else:
        return chr(random.randint(97, 122))


def randomize_string(s, start1, start2, end1, end2):
    result = ""
    for i, c in enumerate(s):
        if c == " ":
            result += " "
        elif i < start1:
            result += randomize_char(c)
        elif i < start2:
            p = (i - start1) / (start2 - start1)
            if random.random() < p:
                result += s[i]
            else:
                result += randomize_char(c)
        elif i < end1:
            result += s[i]
        elif i < end2:
            p = (i - end1) / (end2 - end1)
            if random.random() < p:
                result += s[i]
            else:
                result += randomize_char(c)
        else:
            result += randomize_char(c)
    return result


s = "id just like to interject for a moment what youre referring to as linux is in fact gnu linux or as ive recently taken to calling it gnu plus linux"
window = 20


lines = []
for i in range(-window, len(s), 3):
    start2 = max(0, i)
    start1 = max(0, i - window)
    end1 = min(len(s), i + window)
    end2 = min(len(s), i + window * 2)
    line = randomize_string(s, start1, start2, end1, end2)
    lines.append(line)

# random.shuffle(lines)
print(len(lines))
lines = ['"' + line + '"' for line in lines]
print("\n".join(lines))
