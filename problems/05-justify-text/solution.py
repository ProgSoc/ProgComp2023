def add_word(line: str, word: str) -> str:
    if len(line) == 0:
        return word
    return line + ' ' + word

def text_justification(max_len, text):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        if len(word) <= max_len:
            added = add_word(current_line, word)
            if len(added) <= max_len:
                current_line = added
            else:
                lines.append(current_line)
                current_line = word
        else:
            # If the word is longer than the line
            while len(word) > max_len:
                if current_line:
                    lines.append(current_line)
                    current_line = ""
                lines.append(word[:max_len-1] + '-')
                word = word[max_len-1:]
            current_line = word
    lines.append(current_line.lstrip())  # appending the last line
    return '\n'.join(lines)

max_length = int(input())
line = input()
justified = text_justification(max_length, line)
print(justified)