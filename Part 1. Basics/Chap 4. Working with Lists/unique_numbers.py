""" solution one """

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
new_list = []

for i in range(len(my_list)):
    if i in my_list:
    #    print(i)
        new_list.append(i)

print("The list with unique elements only:")
print(new_list)

#---- Solution 2 --------

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for number in my_list:
    if number not in new_list:
        new_list.append(number)

my_list = new_list[:]
print("The list with unique elements only:")
print(my_list)

