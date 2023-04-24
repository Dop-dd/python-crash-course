""" Looping Through an Entire List """

"""
Let’s say we have a list of magicians’ names, and we want to print out
each name in the list. We could do this by retrieving each name from the
list individually, but this approach could cause several problems. For one,
it would be repetitive to do this with a long list of names. Also, we’d have to
change our code each time the list’s length changed. A for loop avoids both
of these issues by letting Python manage these issues internally.
Let’s use a for loop to print out each name in a list of magicians:
the first line tells Python to retrieve the first value from the list magicians
and associate it with the variable magician. This first value is 'alice'. Python
then reads the next line
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# alice
# david
# carolina

""" Doing More Work Within a for Loop """

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a rgreat trick")

# Alice, that was a rgreat trick
# David, that was a rgreat trick
# Carolina, that was a rgreat trick

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a rgreat trick")
    print(f"I can't wait to see your next trick, {magician.title()}. \n")

# Alice, that was a rgreat trick
# I can't wait to see your next trick, Alice.

# David, that was a rgreat trick
# I can't wait to see your next trick, David.

# Carolina, that was a rgreat trick
# I can't wait to see your next trick, Carolina.

""" Doing Something After a for Loop """

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")