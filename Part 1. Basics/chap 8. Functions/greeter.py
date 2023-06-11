def greet_user():
    print('hello')

greet_user()

print('\n---modified with a value----')

def greet_user(username):
    print(f'hello, {username.title()}')

greet_user('dop')