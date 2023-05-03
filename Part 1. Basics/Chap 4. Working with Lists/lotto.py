
draws = [1, 54, 9, 42, 3, 43, 21]
bets = [5, 54, 9, 16, 3, 43, 85]
hits = 0
winning_nr = []

for number in bets:
    if number in draws:
        winning_nr.append(number)
        hits += 1
print(f"number of hits {hits}")
print(f"actual wining conbimation {winning_nr}")
