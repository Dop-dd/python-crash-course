# list of users and want to print a greeting to each

def greet_users(names):

    for name in names:
        msg = f"hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot', 'tim', 'burntop']

greet_users(usernames)


