"""
Take a look at the snippet:
row = [WHITE_PAWN for i in range(8)]


The part of the code placed inside the brackets specifies:

    the data to be used to fill the list (WHITE_PAWN)
    the clause specifying how many times the data occurs inside the list (for i in range(8))

Let us show you some other list comprehension examples:

Example #1:
squares = [x ** 2 for x in range(10)]


The snippet produces a ten-element list filled with squares of ten integer numbers starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

Example #2:
twos = [2 ** i for i in range(8)]


The snippet creates an eight-element array containing the first eight powers of two (1, 2, 4, 8, 16, 32, 64, 128)

Example #3:
odds = [x for x in squares if x % 2 != 0 ]


The snippet makes a list with only the odd elements of the squares list.

"""



White_pawn = "-"
row = [White_pawn for i in range(8)]

square = [x ** 2 for x in range(8)]
twos = [2 ** i for i in range(8)]
odds = [x for x in square if x % 2 != 0]

row.append(White_pawn)
print(row)
print(square)
print(twos)
print(odds)
