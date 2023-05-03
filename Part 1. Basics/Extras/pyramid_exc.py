blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#
#layer = blocks += 1
level =  1
height = 0

while level <= blocks:
    height += 1
    blocks -= level
    level  += 1

print("The height of the pyramid:", height)

""" second method """

blocks = int(input("Enter the number of blocks: "))

height = 0
in_layer = 1
while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1

print("The height of the pyramid:", height)

