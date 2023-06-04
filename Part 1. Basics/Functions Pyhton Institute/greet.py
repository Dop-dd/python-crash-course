# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)

# introduction("Luke", "Skywalker")
# introduction("Jesse", "Quick")
# introduction("Clark", "Kent")

""" An example of a one-parameter function: """

def hi(name):
    print("hi", name)

hi('don')

""" An example of a one-parameter function: """

def hi_all(name_1, name_2):
    print('hi', name_1)
    print('hi', name_2)

hi_all("macos", "blaze")

""" An example of a three-parameter function: """

def address(street, city, postal_code):
    print("your address is: ", street, "str.", city, postal_code)

s = input("street: ")
p_c = input("postal_code: ")
c = input("city: ")

address(s, c, p_c)
