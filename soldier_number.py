soldier_number = 3
while soldier_number <= 1500:
    if (soldier_number % 3 == 2) and (soldier_number % 5 == 3) and (soldier_number % 7 == 2):
        print("士兵的数量是： %d" % soldier_number)
    soldier_number = soldier_number + 1