def get_greeting(name: str):
    capitalized_name = name.capitalize()
    return f"Hello {capitalized_name}!"


# Read the input
name = input()

# Print the output
print(get_greeting(name))
