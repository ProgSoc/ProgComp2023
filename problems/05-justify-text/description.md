# Text Justification

You are writing a 2D graphics engine, and you want to be able to draw text, but the text needs to wrap around to fit into a given width.

You have the maximum number of characters allowed in a string, and the string itself, and you need to split the text across multiple
lines to fit within the required width.

The text should be split by words, never exceeding the length of the line. If there is a word that's longer than the line itself, then the word should be split with a hyphen. The hyphen shouldn't be outside the line length. For example, if the line length is 10 and the word is 12 characters, then the first 9 characters would be on the first line, then the hyphen, then the remaining 3 characters on the next line.

## Input format

The first line contains a number `N` which is the maximum number of characters allowed in a line.

The second line contains a string `S` which is the text to be justified.

N will be between 2 and 100, inclusive.
S will contain at least one word, and will contain only letters and spaces.

## Output format

Output the text justified to the given width.
