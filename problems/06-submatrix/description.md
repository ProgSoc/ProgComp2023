# Binary Submatrices

Large, unidentified, square objects have been observed passing through the earth's outer atmosphere. The images of these unidentified ojects have been enhanced using a black and white binary threshold, meaning each image contains only black and white pixels.

Black pixels are denoted by `1`, and white pixels are denoted by `0`.

You must write a program that identifies the largest black square by its size and position within the images.

## Input format

The first line contains a number `N`, denoting the width and height of the image with the shape (N, N).

The proceeding lines construct a 2D array, `image`, representing the binary image.

Assume there is at least one occurrence of `1` within the image, all matrices are non-zero.

Assume `N` is between 1 and 10, inclusive.

## Output format

On the first line, print the size of the largest square.

On the second line, print the top-left x/y coordinate of the square in the image
