books = int(input("How many books did you buy this month? "))
if books >= 2 and books < 4:
    print("You earned 5 points.")
elif books >= 4 and books < 6:
    print("You earned 15 points.")
if books >= 6 and books < 8:
    print("You earned 30 points.")
elif books >= 8:
    print("You earned 60 points.")
else:
    print("You earned 0 points.")




