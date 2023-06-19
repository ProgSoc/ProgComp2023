def validate_expression(tokens: list[str]) -> bool:
    # Your code goes here
    pass


tokens = input().split(" ")
is_valid = validate_expression(tokens)
if is_valid:
    print("true")
else:
    print("false")
