# optional middle name

def get_formatted_name(first_name, last_name, middle_name=''):

    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

full_name = get_formatted_name('don', 'mack', 'kenzo')
print(full_name)
full_name = get_formatted_name('don', 'mack')
print(full_name)