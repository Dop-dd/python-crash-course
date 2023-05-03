"""
We can make the parrot.py program run as long as the user wants by putting
most of the program inside a while loop. We’ll define a quit value and then
keep the program running as long as the user has not entered the quit value:
"""
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\Enter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Tell me something, and I will repeat it back to you: \Enter 'quit' to end the program. hi
# hi

# Tell me something, and I will repeat it back to you: \Enter 'quit' to end the program. hee
# hee

# Tell me something, and I will repeat it back to you: \Enter 'quit' to end the program. quit
# quit