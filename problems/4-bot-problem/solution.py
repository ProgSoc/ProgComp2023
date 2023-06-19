import re


def is_spam_bot(username: str) -> bool:
    regex = r"^[A-Z][a-z]+[A-Z][a-z]+\d{3}$"
    return bool(re.search(regex, username))


username_count = int(input())
usernames = [input() for _ in range(username_count)]
for username in usernames:
    if is_spam_bot(username):
        print(username)
