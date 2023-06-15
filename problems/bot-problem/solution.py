import re

# Find how many usernames will be provided
username_count = int(input())

spam_bot_usernames = []
for i in range(username_count):
    username = input()

    # Check if the username is a spam bot
    regex = r"^[A-Z][a-z]+[A-Z][a-z]+\d{3}$"
    if re.search(regex, username):
        spam_bot_usernames.append(username)

# Print the spam bot usernames
for username in spam_bot_usernames:
    print(username)
