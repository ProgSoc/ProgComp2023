# Data recovery

You've found a stash of old tape storage drives from the 90's, however, the data on the tapes has degraded since then and has effectively become corrupted. All the tape drives used to contain the same data, so you've decided to read each drive and combine the corrupted data to recover the oringinal information.

You recieve a list of strings, each string representing the data on a single tape drive. The text on each drive is fairly corrupted, and many characters have turned into other random characters. Spaces always remain as spaces.

For each character, find the most likely character that it should be based on the other tapes. Spaces should be ignored, unless each line contains a space for that character, in which case the resulting character should be a space.

## Input format

The first line contains a number `N` which is the number of tapes.

The next `N` lines contain a string `S` which is the text on a single tape, except surrounded by quotes `""` so that following spaces are not ignored.

`N` will be between 2 and 100, inclusive.

`S` will contain at least one word, and will contain only letters and spaces.

## Output format

Output the recovered text.
