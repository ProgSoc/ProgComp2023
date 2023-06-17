def find_missing_number(arr: list[int]) -> int:
    # Your code goes here
    return missing_number


# Example usage
array = input().split(",")
array = [int(x) for x in array]
missing_number = find_missing_number(array)
print(missing_number)
