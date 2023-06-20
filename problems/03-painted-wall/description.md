# The painted wall

In a developing city, a wall is painted in a repeating sequence of colors: red, green, blue (RGB). The sequence is intended to cycle continuously.

You are given a string representing the wall, where each character is one of 'R', 'G', or 'B', corresponding to red, green, and blue, respectively.

Your task is to calculate how many times the sequence is broken. A sequence is broken when a color does not follow the expected order in the RGB sequence: 'R' is not followed by 'G', 'G' is not followed by 'B', or 'B' is not followed by 'R'.

# Input format
A string that represents the wall. The string only contains the characters R, G, B (uppercase). You can assume the first character of the string is always 'R'

# Output format
An integer representing the number of times the RGB sequence is broken in the string.

Note: When a sequence break occurs, the sequence is expected to continue from the color that caused the break. For example, if 'R' is followed by 'R' (a break because 'R' should be followed by 'G'), we then expect the sequence to continue from this break with 'G' (following the 'R'). If the sequence doesn't resume with the expected color, it's considered another break. Therefore, in the sequence "RGBRRB", there are two breaks: first when 'R' is repeated, and second when 'R' is followed by 'B' instead of the expected 'G'.
