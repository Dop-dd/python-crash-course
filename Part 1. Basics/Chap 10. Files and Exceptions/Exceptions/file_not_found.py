
filename = "'pi_life.txt'"

try:
    with open(filename, encoding='utc-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"\nsorry the file {filename} does not exist")