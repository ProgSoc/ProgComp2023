def is_spam_bot(username: str) -> bool:
    # Your code goes here
    pass


username_count = int(input())
usernames = [input() for _ in range(username_count)]
for username in usernames:
    if is_spam_bot(username):
        print(username)
