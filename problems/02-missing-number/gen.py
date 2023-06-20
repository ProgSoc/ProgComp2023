from random import randint

arrLength = randint(1, 100)

#Fill the array with random numbers in the range 1-arrayLength with no duplicated
arr = [i + 1 for i in range(arrLength)]

# Remove a random number from the array
arr.pop(randint(0, arrLength - 1))

# Shuffle the array
for i in range(arrLength - 1):
    j = randint(0, arrLength - 2)
    arr[i], arr[j] = arr[j], arr[i]

# Print the array length
print(arrLength)

numberStr = ""

# Print the array
for i in range(arrLength - 1):
    numberStr += str(arr[i]) + ","

# Print the last number without comma
# numberStr += str(arr[arrLength - 1])

print(numberStr)
