# break - example

#rint("The break instruction:")
#num = int(input("please enter a number: "))

print("\nbreak statement")
for i in range(1, 10):
    if i == 6:
        break
    print("withinn the loop", i)
print("outside the loop")

print("\ncontinue  statement")
for i in range(1, 10):
    if i == 6:
        continue
    print("withinn the loop", i)
print("outside the loop")
