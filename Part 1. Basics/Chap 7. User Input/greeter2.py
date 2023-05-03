"""
Sometimes you’ll want to write a prompt that’s longer than one line.
For example, you might want to tell the user why you’re asking for certain
input. You can assign your prompt to a variable and pass that variable to the
input() function. This allows you to build your prompt over several lines,
then write a clean input() statement.
"""

prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt +#= "it' just for identifictin, no commercial adverts"
prompt += "\nWhat is your name? "

name = input(prompt)
print(f"\nHello, {name.title()}")

#If you tell us who you are, we can personalize the messages you see.
#What is your name?